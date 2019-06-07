import os
import re
from os.path import join, abspath, splitext, basename

import PyPDF2

regex = re.compile(r'(?i)'              # case insensitive
                   r'^(.*)'             # any number of characters
                   r'(_encrypted)?'     # optional '_encrypted'
                   r'(.pdf)$',          # ends with .pdf
                   re.VERBOSE)


def encrypt_pdfs(path, password):
    path = abspath(path)

    for root, _, files in os.walk(path):
        pdfs = [file for file in files if file.lower().endswith('.pdf')]

        for filename in pdfs:
            filepath = join(abspath(root), filename)
            pdf = open(filepath, 'rb')
            reader = PyPDF2.PdfFileReader(pdf)

            if not reader.isEncrypted:
                writer = PyPDF2.PdfFileWriter()

                for page_num in range(reader.numPages):
                    writer.addPage(reader.getPage(page_num))

                writer.encrypt(password)
                base, ext = splitext(filename)
                new_filepath = join(abspath(root), f'{base}_encrypted{ext}')

                with open(new_filepath, 'wb') as output:
                    writer.write(output)

                pdf.close()
                remove_unencrypted_pdf(new_filepath, filepath, password)


def remove_unencrypted_pdf(encrypted_path, unencrypted_path, password):
    reader = PyPDF2.PdfFileReader(open(encrypted_path, 'rb'))
    if reader.isEncrypted and reader.decrypt(password) == 1:
        os.remove(unencrypted_path)
    else:
        print(f"'{basename(encrypted_path)}' failed the encryption check, "
              f"so '{basename(unencrypted_path)}' was not deleted.")


if __name__ == '__main__':
    encrypt_pdfs('.', 'password')
