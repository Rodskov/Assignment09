import json
from fpdf import FPDF

#Insert your 2x2 picture
class PDF(FPDF):
    def header(self):
        self.image("picture.jpg", 150, 8, 50)
        self.set_font("helvetica", "B", 30)
        self.cell(0, 10, "RESUME", ln=1, align="C")
        self.ln()

#Format the layout of the pdf
pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font("helvetica", '', 16)

#Arrange the texts of the resume
pdf.cell(40, 50, "test")

#Export and make the pdf
pdf.output('DEGUIA_JUSTINCARL.pdf')