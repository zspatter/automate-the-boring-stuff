import os
import re
from os.path import join, abspath, basename
from shutil import copy

import PyPDF2

from pdf_paranoia import pdf_paranoia

original_wd = abspath(os.getcwd())


def test_encrypt_pdfs():
    copy_filenames = ('combinedminutes.pdf',
                      'meetingminutes.pdf',
                      'meetingminutes2.pdf',
                      'watermark.pdf')
    regex = re.compile(r'(?i)'  # case insensitive
                       r'^(.*?)'  # any number of characters (non-greedy)
                       r'(_encrypted)'  # optional '_encrypted'
                       r'(.pdf)$',  # ends with .pdf
                       re.VERBOSE)
    setup_directory(join(abspath('.'), 'pdf_paranoia', 'test_files', 'encrypted'))

    pdf_paranoia.encrypt_pdfs('.', 'password')
    remove_files = []
    for filename, _, pdf_reader in pdf_paranoia.pdf_reader_generator('.'):
        assert regex.search(basename(filename))
        remove_files.append(filename)

    # for file in copy_filenames:
    #     copy(join(abspath('..'), 'sample_files', file), join(abspath('.')))

    revert_directory(remove_files)


# def test_remove_unencrypted_pdf():
#     pass
#
#
# def test_decrypt_pdfs():
#     pass


def test_pdf_reader_generator():
    expected = ('combinedminutes.pdf',
                'meetingminutes.pdf',
                'meetingminutes2.pdf',
                'watermark.pdf',
                'combinedminutes_encrypted.pdf',
                'meetingminutes_encrypted.pdf',
                'meetingminutes2_encrypted.pdf',
                'watermark_encrypted.pdf')
    count = 0
    for filepath, _, _ in pdf_paranoia.pdf_reader_generator(join(abspath('.'),
                                                                 'pdf_paranoia',
                                                                 'test_files')):
        assert basename(filepath) in expected
        count += 1
    # assert count == len(expected)


def test_copy_pdf_pages():
    setup_directory(join(abspath('.'), 'pdf_paranoia', 'test_files', 'unencrypted'))
    reader = PyPDF2.PdfFileReader('combinedminutes.pdf')
    writer = pdf_paranoia.copy_pdf_pages(pdf_reader=reader)
    assert reader.numPages == writer.getNumPages()
    for page_num in range(reader.numPages):
        assert reader.getPage(page_num) == writer.getPage(page_num)
    revert_directory()


def setup_directory(path):
    os.chdir(abspath(path))


def revert_directory(remove_files=()):
    for file in remove_files:
        os.remove(file)

    os.chdir(original_wd)
