import pdfkit
import os, sys

def html_to_pdf(path):
    abs_path = os.path.abspath(path)
    url='file://'+abs_path
    output_path = 'output/out.pdf'
    pdfkit.from_url(url, output_path)
