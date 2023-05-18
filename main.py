import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    cell1 = f"{row['Order']} {row['Topic']} "
    pdf.cell(w=0, h=12, txt=cell1, align="L",
             ln=1, border=0)
    pdf.line(10, 21, 200, 21)
    for i in range(row["Pages"]-1):
        pdf.add_page()

pdf.output("output.pdf")
