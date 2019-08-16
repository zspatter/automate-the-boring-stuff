#! /usr/bin/env python3
# pdf_paranoia.py -


import os
import re
from os.path import join, abspath, splitext, basename, dirname

import PyPDF2


def encrypt_pdfs(path, password):
    """
    Finds all unencrypted PDFs at the given path (and subdirectories) and
    encrypts them with the passed password. After creating an encrypted
    copy, it performs a decryption check with the password. Assuming there
    are no issues with the encryption, the original file is removed.

    :param str path: path to directory to search
    :param str password: password used for encryption
    """
    for filepath, pdf, reader in pdf_reader_generator(path):
        if not reader.isEncrypted:
            writer = copy_pdf_pages(reader)
            writer.encrypt(password)

            base, ext = splitext(basename(filepath))
            new_filepath = join(dirname(abspath(filepath)), f'{base}_encrypted{ext}')

            with open(new_filepath, 'wb') as output:
                writer.write(output)

            pdf.close()
            remove_unencrypted_pdf(new_filepath, filepath, password)


def remove_unencrypted_pdf(encrypted_path, unencrypted_path, password):
    """
    If the file at the encrypted path can be opened with the given password,
    the file at the unencrypted path is removed. Otherwise, an error message
    is displayed indicating which file failed the encryption check.

    :param str encrypted_path: path to encrypted pdf
    :param str unencrypted_path: path to unencrypted (original) pdf
    :param str password: password used for decryption
    """
    reader = PyPDF2.PdfFileReader(open(encrypted_path, 'rb'))
    if reader.isEncrypted and reader.decrypt(password):
        os.remove(unencrypted_path)
    else:
        print(f"'{basename(encrypted_path)}' failed the encryption check, "
              f"so '{basename(unencrypted_path)}' was not deleted.")


def decrypt_pdfs(path, password):
    """
    Finds all encrypted PDFs at the given path (and subdirectories) and
    decrypts them with the passed password.

    :param str path: path to directory to search
    :param str password: password used for encryption
    """
    regex = re.compile(r'(?i)'  # case insensitive
                       r'^(.*?)'  # any number of characters (non-greedy)
                       r'(_encrypted)?'  # optional '_encrypted'
                       r'(\.pdf)$',  # ends with .pdf
                       re.VERBOSE)

    for filepath, pdf, reader in pdf_reader_generator(path):
        if reader.isEncrypted:
            if reader.decrypt(password):
                writer = copy_pdf_pages(reader)

                match_object = regex.search(basename(filepath))
                new_filepath = join(dirname(abspath(filepath)),
                                    f'{match_object.group(1)}{match_object.group(3)}')

                with open(new_filepath, 'wb') as output:
                    writer.write(output)
                pdf.close()

            else:
                print(f"Decryption failed: wrong password provided for '{basename(filepath)}'")


def pdf_reader_generator(path):
    """
    Generator used to generate PDF documents within the path location
    (including subdirectories)

    :param str path: path to directory to search for PDFs
    """
    for root, _, files in os.walk(abspath(path)):
        pdfs = [file for file in files if file.lower().endswith('.pdf')]

        for filename in pdfs:
            filepath = join(abspath(root), filename)
            pdf = open(filepath, 'rb')
            yield filepath, pdf, PyPDF2.PdfFileReader(pdf)


def copy_pdf_pages(pdf_reader):
    """
    Copies all pages from a given pdf reader object to a pdf writer object

    :param pdf_reader: PyPDF2 reader object
    :return: pdf_writer
    """
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

    return pdf_writer


if __name__ == '__main__':
    encrypt_pdfs(join('.', 'sample_files'), 'password')
    decrypt_pdfs(join('.', 'sample_files'), 'password')
