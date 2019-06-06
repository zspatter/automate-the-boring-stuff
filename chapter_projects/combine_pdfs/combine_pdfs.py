#! /usr/bin/env python3
# combine_pdfs.py - Combines all the PDFs in the working directory into a single PDF

import os

import PyPDF2

# finds all PDFs in working directory and sorts by filename
pdfs = [filename for filename in os.listdir() if filename.lower().endswith('.pdf')]
pdfs.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# opens each pdf individually
for filename in pdfs:
    pdf = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf)

    # copies all but the first page to the combined document
    for page_num in range(1, pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

# saves document
with open('combined_pdfs.pdf', 'wb') as output:
    pdf_writer.write(output)
