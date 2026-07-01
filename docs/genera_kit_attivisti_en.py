"""Generate Activist Kit PDF (2 pages) — practical toolkit for civic activists"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Preformatted
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT = os.path.join(os.path.dirname(__file__), "Kit_Attivisti_Sovranita_Digitale_EN.pdf")

BLUE = HexColor("#0066B2")
DARK = HexColor("#212529")
GRAY_BG = HexColor("#F0F3F6")
GRAY_TEXT = HexColor("#6C757D")
WHITE = HexColor("#FFFFFF")
GREEN_LIGHT = HexColor("#F0FFF0")
GREEN_BORDER = HexColor("#5CB85C")

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFont(TTFont("Mono", r"C:\Windows\Fonts\consola.ttf"))

s_label = ParagraphStyle("Label", fontName="Arial-Bold", fontSize=10, textColor=BLUE, spaceAfter=2, leading=12, letterSpacing=2)
s_title = ParagraphStyle("Title", fontName="Arial-Bold", fontSize=18, textColor=DARK, spaceAfter=4, leading=22)
s_subtitle = ParagraphStyle("Subtitle", fontName="Arial", fontSize=9.5, textColor=GRAY_TEXT, spaceAfter=6, leading=12)
s_h1 = ParagraphStyle("H1", fontName="Arial-Bold", fontSize=13, textColor=BLUE, spaceAfter=6, spaceBefore=10, leading=16)
s_body = ParagraphStyle("Body", fontName="Arial", fontSize=9.5, textColor=DARK, spaceAfter=6, leading=13, alignment=TA_JUSTIFY)
s_step_t = ParagraphStyle("StepT", fontName="Arial-Bold", fontSize=10, textColor=BLUE, spaceAfter=2, leading=12)
s_step_b = ParagraphStyle("StepB", fontName="Arial", fontSize=9, textColor=DARK, spaceAfter=6, leading=12)
s_bullet = ParagraphStyle("Bullet", fontName="Arial", fontSize=9, textColor=DARK, spaceAfter=3, leading=12, leftIndent=12)
s_mono = ParagraphStyle("MonoP", fontName="Mono", fontSize=8, textColor=DARK, leading=11)
s_small = ParagraphStyle("Small", fontName="Arial", fontSize=7.5, textColor=GRAY_TEXT, spaceAfter=3, leading=9)
s_box_title = ParagraphStyle("BoxTitle", fontName="Arial-Bold", fontSize=9.5, textColor=BLUE, spaceAfter=3, leading=12)


def footer_func(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, (A4[0] - 20 * mm), 15 * mm)
    canvas.setFont("Arial-Italic", 7)
    canvas.setFillColor(GRAY_TEXT)
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "National Digital Sovereignty Observatory — Activist Kit — CC BY-SA 4.0")
    canvas.drawString(A4[0] - 25 * mm, 10 * mm, f"p. {doc.page}")
    canvas.restoreState()


def box(elements, bg=GRAY_BG, border_color=None):
    style = [("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 10),
             ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("ROUNDEDCORNERS", [3, 3, 3, 3])]
    if border_color:
        style.append(("LINEBEFORE", (0, 0), (0, -1), 3, border_color))
    t = Table([[elements]], colWidths=[170 * mm])
    t.setStyle(TableStyle(style))
    return t


def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=22 * mm)
    story = []

    story.append(Paragraph("ACTIVIST KIT", s_label))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Act on the Digital Sovereignty<br/>of your Public Administration", s_title))
    story.append(Paragraph("Practical tools for active citizens — "
                           "National Digital Sovereignty Observatory", s_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=8, spaceBefore=2))

    story.append(Paragraph("Why your action matters", s_h1))
    story.append(Paragraph(
        "You do not need to be a technology expert. When a citizen asks their own municipality where "
        "their emails end up, the administration is forced to ask itself the question. Civic pressure, "
        "multiplied, becomes institutional awareness and then action.", s_body))

    story.append(Paragraph("Four concrete steps", s_h1))
    for t, b in [
        ("1. Check your public body",
         "Look up your municipality, local health authority or school in the Observatory data and find out which provider manages the email and under which jurisdiction."),
        ("2. Ask the right question",
         "Write to the body and ask which email provider it uses, where the data is stored and whether a jurisdictional risk assessment has been carried out."),
        ("3. Spread the data",
         "Share the results on social media and with the local press: \"where our municipality's emails end up\" is a story with strong local impact."),
        ("4. Bring the topic to the council",
         "Propose a motion or a question on the body's digital sovereignty to a municipal councillor, using the data as a basis."),
    ]:
        story.append(Paragraph(t, s_step_t))
        story.append(Paragraph(b, s_step_b))

    story.append(Spacer(1, 1 * mm))
    story.append(box([
        Paragraph("Key messages", s_box_title),
        Paragraph("•  \"Your data can end up on servers subject to foreign laws.\"", s_bullet),
        Paragraph("•  \"Digital sovereignty means: who controls citizens' data.\"", s_bullet),
        Paragraph("•  \"It is not against a provider: it is in favour of public control over public data.\"", s_bullet),
        Paragraph("•  \"Compliant European alternatives exist. What is needed is the will to use them.\"", s_bullet),
    ], GREEN_LIGHT, GREEN_BORDER))

    # ── PAGE 2 ──
    story.append(PageBreak())
    story.append(Paragraph("Freedom of information access request template", s_h1))
    story.append(Paragraph(
        "You can use the generalised civic access right (art. 5, c. 2, D.Lgs. 33/2013) to obtain "
        "information from the body. Adapt the following text to your case:", s_body))

    fac = ("Subject: Generalised civic access request\n"
           "(art. 5, c. 2, D.Lgs. 33/2013)\n\n"
           "The undersigned [name] requests to know:\n\n"
           "1. which provider manages the body's email\n"
           "   service;\n"
           "2. in which country the email data is stored;\n"
           "3. whether the provider is subject to non-EU\n"
           "   legislation allowing access by foreign\n"
           "   authorities (e.g. the US CLOUD Act);\n"
           "4. whether a data protection impact assessment\n"
           "   (DPIA) has been carried out for this service.\n\n"
           "Kind regards,\n"
           "[name, place, date]")
    story.append(box([Preformatted(fac, s_mono)]))
    story.append(Paragraph("Informational template, to be adapted to the specific case. It does not "
                           "constitute legal advice.", s_small))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Where to find the data and coordinate", s_h1))
    story.append(Paragraph("•  <b>Data and reports</b>: the Observatory website and its downloadable documents", s_bullet))
    story.append(Paragraph("•  <b>Detailed data by public body</b>: MxMap.it", s_bullet))
    story.append(Paragraph("•  <b>Coordination</b>: the Observatory's Telegram channel", s_bullet))
    story.append(Paragraph("•  <b>Reports and proposals</b>: the project's GitHub Issues", s_bullet))

    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#DEE2E6"), spaceAfter=3, spaceBefore=2))
    story.append(Paragraph("National Digital Sovereignty Observatory — "
                           "https://osservatorio.mxmap.it/ — "
                           "CC BY-SA 4.0 document.", s_small))

    doc.build(story, onFirstPage=footer_func, onLaterPages=footer_func)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
