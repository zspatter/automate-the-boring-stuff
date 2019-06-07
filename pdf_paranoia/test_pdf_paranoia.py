import os
from os.path import join, abspath

from pdf_paranoia import pdf_paranoia

original_wd = abspath(os.getcwd())


def test_encrypt_pdfs():
    pass


def test_remove_unencrypted_pdf():
    pass


def test_decrypt_pdfs():
    pass


def test_pdf_reader_generator():
    count = 0
    for pdf in pdf_paranoia.pdf_reader_generator(join(abspath('.'),
                                                      'pdf_paranoia',
                                                      'test_files')):
        count += 1
    assert count == 8


def test_copy_pdf_pages():
    pass


def setup_directory(path):
    os.chdir(abspath(path))


def revert_directory(remove_files):
    for file in remove_files:
        os.remove(file)

    os.chdir(original_wd)
