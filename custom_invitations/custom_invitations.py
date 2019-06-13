from os.path import abspath, join

import docx
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
# from docx.text import Run


def generate_invitations(textfile: str, filename: str) -> None:
    """
    Generates a custom invitation for each name in the given text file.
    Each individual invitation corresponds to a single page in the .docx

    :param str textfile: path to .txt file
    :param str filename: path to .docx file
    """
    doc = docx.Document()

    with open(textfile, 'r') as guests:
        # generates a custom inviation for each guest
        for guest in guests:
            paragraph1 = doc.add_paragraph()
            paragraph1.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            style_run(run=paragraph1.add_run('It would be a pleasure to have the company of'),
                      is_bold=True,
                      is_italic=True,
                      font_size=13)

            paragraph2 = doc.add_paragraph()
            paragraph2.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            style_run(run=paragraph2.add_run(guest.strip()),
                      is_bold=True,
                      font_size=15)

            paragraph3 = doc.add_paragraph()
            paragraph3.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            style_run(run=paragraph3.add_run('at 11101 Memory lane on the evening of'),
                      is_bold=True,
                      is_italic=True)

            paragraph4 = doc.add_paragraph()
            paragraph4.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            style_run(run=paragraph4.add_run('April 31st'))

            paragraph5 = doc.add_paragraph()
            paragraph5.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            style_run(run=paragraph5.add_run("at 24 O'Clock"),
                      is_bold=True,
                      is_italic=True)

            doc.add_page_break()

    doc.save(filename)


def style_run(run, is_bold: bool = None, is_italic: bool = None, font_size: int = 12) -> None:
    """
    Applies rich text styles to the given Run text object.

    :param Run run: run of text to be style
    :param bool is_bold: indicates if run should be bold
    :param bool is_italic: indicates if run should be italic
    :param int font_size: indicates font size
    """
    run.font.bold = is_bold
    run.font.italic = is_italic
    run.font.size = Pt(font_size)


if __name__ == '__main__':
    path = join(abspath('.'), 'sample_files')
    generate_invitations(textfile=join(path, 'guests.txt'),
                         filename=join(path, 'invitations.docx'))
