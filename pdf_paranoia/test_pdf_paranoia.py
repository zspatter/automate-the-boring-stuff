from os.path import join, abspath

from pdf_paranoia import pdf_paranoia


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
