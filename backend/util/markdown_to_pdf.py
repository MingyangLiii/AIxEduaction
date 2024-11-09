import pdfkit
from markdown import markdown


def markdown_to_pdf(input_md, output_pdf):
    with open(input_md, encoding='utf-8') as f:
        text = f.read()
    html = markdown(text, output_format='html')
    pdfkit.from_string(html, output_pdf)