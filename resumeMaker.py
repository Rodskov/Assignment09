import json
from fpdf import FPDF

#Format the layout of the pdf
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font("helvetica", '', 16)

#Arrange the texts of the resume
pdf.cell(40, 10, "TEST")

#Export and make the pdf
pdf.output('DEGUIA_JUSTINCARL.pdf')