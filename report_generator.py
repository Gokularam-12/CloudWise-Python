from fpdf import FPDF

def generate_report(actions, total_savings, output_path="reports/optimization_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="CloudWise Optimization Report", ln=True, align='C')
    pdf.ln(10)
    for action, saving in actions:
        pdf.cell(200, 10, txt=f"{action} -> Save ₹{int(saving)}", ln=True)
    
    pdf.ln(10)
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Estimated Monthly Savings: ₹{int(total_savings)}", ln=True)
    pdf.output(output_path)
