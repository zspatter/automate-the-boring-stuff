from os.path import abspath, basename, join

import PyPDF2


def break_password(encrypted_pdf, pw_list):
    pdf = PyPDF2.PdfFileReader(open(abspath(encrypted_pdf), 'rb'))
    print(f"Attempting to decrypt '{basename(encrypted_pdf)}' via brute force")

    with open(abspath(pw_list), 'r') as reader:
        passwords = reader.read().split('\n')

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
    output = f"\nSuccess!\nThe password is: '{result}'" if result else \
        f"\nFailure!\nFailed to decrypt the pdf"
    print(output)
