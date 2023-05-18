import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    cell1 = f"{row['Order']} {row['Topic']} "
    pdf.cell(w=0, h=12, txt=cell1, align="L",
             ln=1, border=0)
    pdf.line(10, 21, 200, 21)
    for l in range(3, 27):  # or range(3, 27, 10)
        pdf.line(10, 10 * l, 200, 10 * l)
# set the footer
    pdf.ln(246)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(258)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        # add page line
        for l in range(2, 28):
            pdf.line(10, 10*l, 200, 10*l)

pdf.output("output.pdf")
