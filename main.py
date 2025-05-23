from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for _, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200 ,20)

    pdf.ln(260)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.ln(260)
        pdf.set_font('Arial', 'I', 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row["Topic"], align="R")

pdf.output("output1.pdf")


#
#
#
# pdf.set_font('Arial', 'B', 16)
# pdf.cell(w=0, h=12, txt="Hello World!", align="L", ln=1, border=0,)
# pdf.cell(w=0, h=12, txt="Hi2 World!", align="L", ln=1, border=0,)
#
#