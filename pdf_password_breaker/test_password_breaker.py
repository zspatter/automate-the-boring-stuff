from os.path import abspath, join

import PyPDF2

from pdf_password_breaker import password_breaker

root = abspath(join('.', 'pdf_password_breaker', 'test_files'))

valid_matches = ('SPECIAL!@#$',
                 'MIXEDcase',
                 'SAMPLE_PASSWORD!')
invalid_matches = ('invalid_password',
                   'doesNOTmatchPWlist')


def test_break_password():
    # break open valid matches from textfile
    for password in valid_matches:
        encrypt_pdf(password)
        result = password_breaker.break_password(encrypted_pdf=join(root, 'test_pdf.pdf'),
                                                 pw_list=join(root, 'passwords.txt'))
        assert result == password

    # fail to break open invalid matches
    for password in invalid_matches:
        encrypt_pdf(password)
        result = password_breaker.break_password(encrypted_pdf=join(root, 'test_pdf.pdf'),
                                                 pw_list=join(root, 'passwords.txt'))
        assert not result


def encrypt_pdf(password):
    writer = PyPDF2.PdfFileWriter()
    writer.encrypt(password)
    with open(file=join(root, 'test_pdf.pdf'), mode='wb') as pdf_file:
        writer.write(pdf_file)
