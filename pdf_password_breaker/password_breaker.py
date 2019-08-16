#! /usr/bin/env python3
# password_breaker.py - simple program that attempts to brute force encrypted PDF

from os.path import abspath, basename, join

import PyPDF2


def break_password(encrypted_pdf, pw_list):
    """
    Attempts to decrypt an encrypted PDF via brute force. The passwords
    used are lines in the text file at the pw_list path. Each password
    is attempted in it's current case as well as upper/lower case.

    :param str encrypted_pdf: path to PDF to decrypt
    :param str pw_list: path to text file of passwords
    :return: valid password (or None)
    """
    pdf = PyPDF2.PdfFileReader(open(abspath(encrypted_pdf), 'rb'))
    print(f"Attempting to decrypt '{basename(encrypted_pdf)}' via brute force...")

    with open(abspath(pw_list), 'r') as reader:
        passwords = reader.read().split()

    # checks default case, lower, then upper
    for password in passwords:
        if pdf.decrypt(password):
            return password
        elif pdf.decrypt(password.lower()):
            return password.lower()
        elif pdf.decrypt(password.upper()):
            return password.upper()


if __name__ == '__main__':
    # gathers absolute paths of the files
    pdf_path = abspath(join('.', 'sample_files', 'encrypted_pdf.pdf'))
    passwords_path = abspath(join('.', 'sample_files', 'dictionary.txt'))

    # generates an empty, encrypted PDF
    writer = PyPDF2.PdfFileWriter()
    writer.encrypt('abnormality')
    with open(file=pdf_path, mode='wb') as pdf_file:
        writer.write(pdf_file)

    # attempts to decrypt the file and prints the results
    result = break_password(encrypted_pdf=pdf_path, pw_list=passwords_path)
    print(f"\nSuccess!\nThe password is: '{result}'" if result else
          "\nFailure!\nFailed to decrypt the PDF")
