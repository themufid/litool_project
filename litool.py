# Almufid Official License
# Copyright (c) 2024 Almufid Official
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# You are not allowed to use the name "Almufid Official" or any other copyright holder names for the purpose of promotion or endorsement without prior written permission.
# 
# You must include a reference to Almufid Official in all materials published or presented that use this software.

import argparse
import sys
from core.scanner import Scanner
from core.injector import Injector
from utils.logger import Logger
from fpdf import FPDF

def save_results_to_pdf(results, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Scan Results", ln=True, align="C")
    for result in results:
        pdf.cell(200, 10, txt=result, ln=True, align="L")
    pdf.output(output_file)

def main():
    parser = argparse.ArgumentParser(description="litool - Simple SQL Injection Tool")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--scan", help="Scan for vulnerabilities", action="store_true")
    parser.add_argument("--inject", help="Perform automatic exploitation", action="store_true")
    parser.add_argument("--output", help="Output file to save scan results (without extension)")
    parser.add_argument("--timeout", help="HTTP request timeout in seconds", type=int, default=10)
    args = parser.parse_args()

    logger = Logger()

    if args.scan:
        scanner = Scanner(args.url, logger)
        scanner.set_timeout(args.timeout)
        results = scanner.scan()
        if args.output:
            txt_output = f"results/{args.output}.txt"
            pdf_output = f"results/{args.output}.pdf"
            with open(txt_output, "w") as f:
                f.write("\n".join(results))
            save_results_to_pdf(results, pdf_output)

    if args.inject:
        injector = Injector(args.url, logger)
        injector.set_timeout(args.timeout)
        results = injector.inject()
        if args.output:
            txt_output = f"results/{args.output}_inject.txt"
            pdf_output = f"results/{args.output}_inject.pdf"
            with open(txt_output, "w") as f:
                f.write("\n".join(results))
            save_results_to_pdf(results, pdf_output)

if __name__ == "__main__":
    main()
