#!/bin/bash
# Registro attività e bot Telegram — esecuzione sul server (cron dell'utente ubuntu).
#
#   server.sh installa   prepara $DATA (env con sale, venv, clone del repo) — idempotente
#   server.sh ciclo      raccolta + sintesi + post live + riepilogo delle 8:30; commit e push
#   server.sh poll       legge i messaggi nuovi della comunità Telegram
#   server.sh statistiche  statistiche di accesso ai siti (GoatCounter) → data/statistiche; commit e push
#
# Crontab (ora del server = Europe/Rome):
#   */5 * * * *  ~/.local/share/osservatorio-bot/repo/tools/registro/server.sh poll
#   15 * * * *   ~/.local/share/osservatorio-bot/repo/tools/registro/server.sh ciclo
#   30 8 * * *   ~/.local/share/osservatorio-bot/repo/tools/registro/server.sh ciclo
#   10 5 * * *   ~/.local/share/osservatorio-bot/repo/tools/registro/server.sh statistiche
#
# Statistiche: GoatCounter (servizio systemd `goatcounter`, utente goatcounter, dati in
# /var/lib/goatcounter, dietro Caddy su stats.mxmap.it). statistiche.py ne legge una copia
# con `sudo -u goatcounter sqlite3 .backup` (ubuntu ha sudo senza password).
#
# Il bot lavora su un CLONE dedicato ($DATA/repo), così non tocca mai la copia
# di lavoro di chi sviluppa. Segreti in $DATA/env (permessi 600, fuori da git):
#   TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID (gruppo: solo riepiloghi settimanali),
#   TELEGRAM_FEED_ID (canale @osservatoriops: live e giornaliero), TELEGRAM_COMMUNITY_ID
#   (gruppo da misurare), COMUNITA_SALT (generato), REGISTRO_MOTORE=cli.
set -uo pipefail
DATA="${OSSERVATORIO_BOT_DATA:-$HOME/.local/share/osservatorio-bot}"
export OSSERVATORIO_BOT_DATA="$DATA"
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin"
REPO="$DATA/repo"
PY="$DATA/venv/bin/python"
URL="https://github.com/mxmap-it/osservatorio-nazionale-sovranita-digitale.git"
modo="${1:-}"
mkdir -p "$DATA/log"

if [ "$modo" = installa ]; then
  umask 077
  if [ ! -f "$DATA/env" ]; then
    cat > "$DATA/env" <<EOF
# Bot del Registro attività — segreti (non in git)
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
TELEGRAM_FEED_ID=@osservatoriops
TELEGRAM_COMMUNITY_ID=
COMUNITA_SALT=$(head -c 32 /dev/urandom | od -An -tx1 | tr -d ' \n')
REGISTRO_MOTORE=cli
EOF
  fi
  chmod 600 "$DATA/env"
  [ -x "$PY" ] || python3 -m venv "$DATA/venv"
  "$PY" -m pip install --quiet --upgrade pip 'matplotlib>=3.8'
  [ -d "$REPO/.git" ] || git clone -q "$URL" "$REPO"
  git -C "$REPO" config user.name "osservatorio-registro[bot]"
  git -C "$REPO" config user.email "noreply@osservatorio.mxmap.it"
  echo "installato in $DATA"
  exit 0
fi

set -a; . "$DATA/env"; set +a
export REGISTRO_MOTORE="${REGISTRO_MOTORE:-cli}"
log="$DATA/log/$modo.log"
exec 9>"$DATA/.lock-$modo"
flock -n 9 || exit 0   # il giro precedente è ancora in corso
exec >>"$log" 2>&1
echo "── $(date '+%F %T') $modo"

case "$modo" in
  poll)
    [ -n "${TELEGRAM_BOT_TOKEN:-}" ] || exit 0
    "$PY" "$REPO/tools/registro/comunita.py" poll
    ;;
  ciclo)
    cd "$REPO" || exit 1
    git pull -q --rebase --autostash || { echo "pull fallito"; exit 1; }
    "$PY" tools/registro/registro.py ciclo --motore "$REGISTRO_MOTORE"
    git add data/registro data/statistiche tools/registro/stato-telegram.json
    if ! git diff --cached --quiet; then
      git commit -q -m "Registro attività: aggiornamento automatico" -m "Generato da tools/registro/server.sh sul server."
      for i in 1 2 3; do git pull -q --rebase && git push -q && break; sleep 10; done
    fi
    ;;
  statistiche)
    cd "$REPO" || exit 1
    git pull -q --rebase --autostash || { echo "pull fallito"; exit 1; }
    "$PY" tools/registro/statistiche.py pubblica
    git add data/statistiche
    if ! git diff --cached --quiet; then
      git commit -q -m "Statistiche di accesso: aggiornamento automatico" -m "Generato da tools/registro/server.sh sul server."
      for i in 1 2 3; do git pull -q --rebase && git push -q && break; sleep 10; done
    fi
    # geolocalizzazione (DB-IP City Lite, CC BY 4.0): nuova edizione il 2 di ogni mese
    if [ "$(date +%d)" = "02" ]; then
      f="/tmp/dbip-$$.mmdb"
      if curl -sfL "https://download.db-ip.com/free/dbip-city-lite-$(date +%Y-%m).mmdb.gz" | gunzip > "$f" && [ -s "$f" ]; then
        sudo -n install -o goatcounter -g goatcounter -m 644 "$f" /var/lib/goatcounter/dbip-city-lite.mmdb \
          && sudo -n systemctl restart goatcounter && echo "geodb aggiornato"
      fi
      rm -f "$f"
    fi
    ;;
  *)
    echo "uso: $0 installa|ciclo|poll|statistiche"; exit 2 ;;
esac
# log corti: si tengono le ultime 5000 righe
tail -n 5000 "$log" > "$log.tmp" && mv "$log.tmp" "$log"
