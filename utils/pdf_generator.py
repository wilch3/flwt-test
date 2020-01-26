"""Script for generating a pdf."""
from fpdf import FPDF


def generate_pdf(path, data):
    """Generates pdf.

    :param path: path to generated pdf
    :param data: readable information about the order
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.image("utils/temp/barcode.png", x=10, y=10, w=80, h=30)  # barcode.png stores data in Code128 format
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=data, ln=2, align="R")
    pdf.output(f"{path}", "F")
