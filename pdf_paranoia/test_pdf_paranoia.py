import os
import re
from os.path import join, abspath, basename
from shutil import copy

import PyPDF2

from pdf_paranoia import pdf_paranoia

valid_password = 'password'
invalid_password = 'wrong password'
encrypted_regex = re.compile(r'(?i)'                # case insensitive
                             r'^(.*?)'              # any number of characters (non-greedy)
                             r'(_encrypted)'        # optional '_encrypted'
                             r'(\.pdf)$',            # ends with .pdf
                             re.VERBOSE)
unencrypted_regex = re.compile(r'(?i)'              # case insensitive
                               r'^(.*?)'            # any number of characters (non-greedy)
                               r'(?<!_encrypted)'   # does not include _encrypted
                               r'(\.pdf)$',         # ends with .pdf
                               re.VERBOSE)


def test_encrypt_pdfs():
    copy_filenames = ('combinedminutes.pdf',
                      'meetingminutes.pdf',
                      'meetingminutes2.pdf',
                      'watermark.pdf')
    path = join(abspath('.'), 'pdf_paranoia', 'test_files', 'unencrypted')
    pdf_paranoia.encrypt_pdfs(path, valid_password)
    file_list = []

    # verify all PDF files are now encrypted with the desired password
    for filename, _, pdf_reader in pdf_paranoia.pdf_reader_generator(path):
        assert encrypted_regex.search(basename(filename))
        assert pdf_reader.isEncrypted
        assert not pdf_reader.decrypt(invalid_password)
        assert pdf_reader.decrypt(valid_password)
        file_list.append(filename)

    # copy unencrypted files to directory (replace the removed files)
    for file in copy_filenames:
        copy(join(abspath('.'), 'pdf_paranoia', 'sample_files', file), path)

    # remove encrypted files
    for file in file_list:
        os.remove(file)


def test_remove_unencrypted_pdf():
    encrypted_path = join(abspath('.'), 'pdf_paranoia', 'test_files', 'encrypted')
    unencrypted_path = join(abspath('.'), 'pdf_paranoia', 'test_files', 'unencrypted')
    filename = os.listdir(unencrypted_path)[0]

    # verify file exists and filecount is as expected
    assert os.path.exists(join(unencrypted_path, filename))
    assert len(os.listdir(unencrypted_path)) == 4

    # remove unencrypted file (valid password)
    pdf_paranoia.remove_unencrypted_pdf(join(encrypted_path, os.listdir(encrypted_path)[0]),
                                        join(unencrypted_path, os.listdir(unencrypted_path)[0]),
                                        password=valid_password)

    # verify file was removed and next file'a path exists
    assert not os.path.exists(join(unencrypted_path, filename))
    assert len(os.listdir(unencrypted_path)) == 3
    assert os.path.exists(join(unencrypted_path, os.listdir(unencrypted_path)[1]))

    # fail encryption check - doesn't remove unencrypted file (invalid password)
    pdf_paranoia.remove_unencrypted_pdf(join(encrypted_path, os.listdir(encrypted_path)[1]),
                                        join(unencrypted_path, os.listdir(unencrypted_path)[1]),
                                        password=invalid_password)

    # verify file still exists and file count remains unchanged
    assert os.path.exists(join(unencrypted_path, os.listdir(unencrypted_path)[1]))
    assert len(os.listdir(unencrypted_path)) == 3

    # replace removed file
    source = join(abspath('.'), 'pdf_paranoia', 'sample_files', filename)
    destination = join(abspath('.'), 'pdf_paranoia', 'test_files', 'unencrypted')
    copy(source, destination)


def test_decrypt_pdfs():
    path = join(abspath('.'), 'pdf_paranoia', 'test_files', 'encrypted')
    assert len(os.listdir(path)) == 4

    # verify invalid password fails
    pdf_paranoia.decrypt_pdfs(path, invalid_password)
    assert len(os.listdir(path)) == 4

    pdf_paranoia.decrypt_pdfs(path, valid_password)
    assert len(os.listdir(path)) == 8

    # removes the decrypted files
    for file in os.listdir(path):
        if unencrypted_regex.search(file):
            os.remove(join(path, file))


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

    # verify results are expected files
    for filepath, _, _ in pdf_paranoia.pdf_reader_generator(join(abspath('.'),
                                                                 'pdf_paranoia',
                                                                 'test_files')):
        assert basename(filepath) in expected
        count += 1
    # verify expected number of matches
    assert count == len(expected)


def test_copy_pdf_pages():
    filepath = join(abspath('.'), 'pdf_paranoia', 'test_files', 'unencrypted',
                    'combinedminutes.pdf')
    reader = PyPDF2.PdfFileReader(open(filepath, 'rb'))
    writer = pdf_paranoia.copy_pdf_pages(pdf_reader=reader)
    assert reader.numPages == writer.getNumPages()

    # verify contents are identical between reader and writer
    for page_num in range(reader.numPages):
        assert reader.getPage(page_num) == writer.getPage(page_num)
