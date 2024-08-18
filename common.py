from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt


# Create the 'pgMar' element with the appropriate margins
def set_margin():
    margin_cm = 1.27
    margin_twips = int(margin_cm * 567)
    pgMar = OxmlElement("w:pgMar")
    pgMar.set(qn("w:top"), str(margin_twips))
    pgMar.set(qn("w:right"), str(margin_twips))
    pgMar.set(qn("w:bottom"), str(margin_twips))
    pgMar.set(qn("w:left"), str(margin_twips))
    pgMar.set(qn("w:header"), "720")  # Default header margin
    pgMar.set(qn("w:footer"), "720")  # Default footer margin
    pgMar.set(qn("w:gutter"), "0")  # No gutter margin
    return pgMar


def stylize(header_run, font="Times New Roman", size=18, bold=False, italic=False):
    header_run.font.name = font
    header_run.font.size = Pt(size)
    header_run.bold = bold
    header_run.italic = italic
