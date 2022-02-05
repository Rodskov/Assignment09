import json
from fpdf import FPDF

#Insert your 2x2 picture
class PDF(FPDF):
    def header(self):
        self.set_fill_color(r=229, g=228, b=226) #Gray Rectangle
        self.rect(x=10, y=8, w=150, h=78, style="FD") #horizontal
        self.rect(x=123, y=8, w=78.5, h=250, style="FD") #vertical
        self.set_fill_color(r=0, g=145, b=234) #Sky Blue Rectangle
        self.rect(x=123, y=8, w=78.5, h=78, style="FD") #portrait background
        self.image("picture.jpg", 125, 9.5, 75)
        self.set_font("helvetica", "B", 30)
        self.ln()
        
#Format the layout of the pdf
pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()

#Load in the json file
with open('resume.json') as f:
    data = json.load(f)

#Arrange the texts of the resume
for info in data:
    #Part 1: Arrange the name, job, and profile
    pdf.ln(42)
    pdf.set_text_color(r=0, g=145, b=234)
    pdf.set_font("times", 'B', 36)
    pdf.cell(100, 10, info['firstName'], ln=1)
    pdf.cell(100, 10, info['lastName'], ln=1)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font("times", 'I', 20)
    pdf.cell(45, 10, info['job'])
    pdf.cell(50, 10, f", {info['age']}", ln=3)

    #Part 2: Arrange the contacts and additional info
    pdf.ln(10)
    pdf.set_font("times", 'B', 20)
    pdf.cell(116, 10, "Additional Info:")
    pdf.cell(116, 10, "Contact Info:", ln=1)
    pdf.set_font("times", 'B', 16)
    pdf.cell(116, 10, "Skills:")
    pdf.set_font("times", '', 16)
    pdf.cell(90, 10, f"Contact Number: {info['contactNum']}", ln=1)
    for skill in info['skills']:
        pdf.cell(10, 10, f"- {skill}", ln=1)
    pdf.set_font("times", 'B', 16)
    pdf.cell(116, 10, "Hobbies:")
    pdf.set_font("times", '', 16)
    pdf.cell(190, 10, f"Github: {info['github']}", ln=1)
    for hobby in info['hobbies']:
        pdf.cell(10, 10, f"- {hobby}", ln=1)
    pdf.set_font("times", 'B', 16)
    pdf.cell(116, 10,"Educational Attainment:")
    pdf.set_font("times", '', 16)
    pdf.cell(190, 10, f"Email: {info['email']}", ln=1)
    for level in info['educ']:
        pdf.set_font("times", '', 16)
        pdf.cell(100, 10, f"{level['school']}", ln=1)
        pdf.set_font("times", 'I', 16)
        pdf.cell(190, 10, f"- {level['year']}", ln=1)

#Draw lines to design
pdf.set_line_width(2)
pdf.set_draw_color(r=0, g=145, b=234)
pdf.line(x1=12.5, y1=82, x2=30, y2=82) #College Student Line
pdf.line(x1=12.5, y1=102, x2=30, y2=102) #Additional Info Line
pdf.line(x1=128.5, y1=102, x2=150, y2=102) #Contact Info Line

#Export and make the pdf
pdf.output('DEGUIA_JUSTINCARL.pdf')