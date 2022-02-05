import json
from fpdf import FPDF

#Insert your 2x2 picture
class PDF(FPDF):
    def header(self):
        self.image("picture.jpg", 150, 8, 50)
        self.set_font("helvetica", "B", 30)
        self.cell(0, 10, "RESUME", ln=1, align="C")
        self.ln()

    def body(self):
        self.set_font("helvetica", '', 12)
        
#Format the layout of the pdf
pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font("helvetica", '', 16)

#Load in the json file
with open('resume.json') as f:
    data = json.load(f)

#Arrange the texts of the resume
for info in data:
    pdf.cell(100, 10, f"Name: {info['name']}", border=True, ln=1)
    pdf.cell(100, 10, f"Age: {info['age']}", border=True, ln=1)
    pdf.cell(100, 10, f"Job: {info['job']}", border=True, ln=1)
    pdf.cell(190, 10, f"Contact Number: {info['contactNum']}", border=True, ln=1)
    pdf.cell(190, 10, f"Email: {info['email']}", border=True, ln=1)
    pdf.ln()
    pdf.ln()
    pdf.cell(190, 10, f"Skills: {info['skills']}", ln=1)
    pdf.ln()
    pdf.cell(190, 10, f"Hobbies: {info['hobbies']}", ln=1)
    pdf.ln()
    pdf.cell(190, 10, f"Educational Attainment: {info['educAttain']}", ln=1)

#Export and make the pdf
pdf.output('DEGUIA_JUSTINCARL.pdf')