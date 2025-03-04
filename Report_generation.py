import pandas as pd
from fpdf import FPDF
import os

def read_data(file_path):
    """Reads data from a CSV file."""
    return pd.read_csv(file_path)

def analyze_data(df):
    """Performs basic analysis on the dataset."""
    summary = df.describe()
    return summary

def generate_pdf_report(summary, output_file):
    """Generates a PDF report from the analyzed data."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Data Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for column in summary.columns:
        pdf.cell(200, 10, f"Column: {column}", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 7, summary[column].to_string(), align='L')
        pdf.ln(5)
        pdf.set_font("Arial", size=12)
    
    pdf.output(output_file)

def main():
    input_file = "C:\\Users\\len S5(22IN)\\Desktop\\python program\\patterns\\Internship_task\\education_career_success.csv"
    output_file = "eduction_report.pdf"
    
    df = read_data(input_file)
    summary = analyze_data(df)
    generate_pdf_report(summary, output_file)
    
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    main()
