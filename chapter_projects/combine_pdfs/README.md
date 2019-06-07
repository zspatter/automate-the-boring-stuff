# Combining Select Pages from Many PDFs

Say you have the boring job of merging several dozen PDF documents into a single PDF file. Each of them has a cover sheet as the first page, but you don’t want the cover sheet repeated in the final result. Even though there are lots of free programs for combining PDFs, many of them simply merge entire files together. Let’s write a Python program to customize which pages you want in the combined PDF.

At a high level, here’s what the program will do:
- Find all PDF files in the current working directory
- Sort the filenames so the PDFs are added in order
- Write each page, excluding the first page, of each PDF to the output file

## Ideas for Similar Programs

Being able to create PDFs from the pages of other PDFs will let you make programs that can do the following:

- Cut out specific pages from PDFs
- Reorder pages in a PDF
- Create a PDF from only those pages that have some specific text, identified by extractText()
