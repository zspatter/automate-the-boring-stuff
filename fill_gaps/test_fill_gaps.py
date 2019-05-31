import os
import re
import shutil

from fill_gaps import fill_gaps

expected_matches = ('__init__.py',
                    'fill_gaps.py',
                    'test_fill_gaps.py')
expected_gaps = ('spam001.txt',
                 'spam003.txt',
                 'spam005.txt',
                 'spam007.txt',
                 'spam009.txt')
expected_fill = ('spam001.txt',
                 'spam002.txt',
                 'spam003.txt',
                 'spam004.txt',
                 'spam005.txt')


def test_get_matching_files():
    root = os.path.abspath('./fill_gaps/')

    matches = fill_gaps.get_matching_files(root=root,
                                           regex=re.compile(r'(^.*)(\.py$)'))
    py_files = [file for file in os.listdir(root) if file.endswith('.py')]

    assert len(matches) == len(expected_matches)
    assert len(py_files) == len(matches)

    for match in matches:
        assert match in expected_matches
        assert match in py_files


def test_fill_sequence_gaps():
    # dir at path created
    path = os.path.abspath(os.path.join('.', 'fill_gaps', 'test_files'))
    os.makedirs(path)

    # creates files with only odd numbers spam00<x>.txt
    for x in range(1, 10, 2):
        with open(os.path.join(path, f'spam00{x}.txt'), 'w') as spam:
            spam.write(f'spam00{x}')

    # files created prior to filling gaps
    gap_files = os.listdir(path)
    for gap_file in gap_files:
        assert gap_file in expected_gaps

    # results after filling gaps
    fill_gaps.fill_sequence_gap(path, 'spam', '.txt')
    fill_files = os.listdir(path)
    regex = re.compile(r'(^spam)(\d+)(.*)?(\.txt$)')

    # verifies files are renamed as expected and  contents remain unchanged
    for fill_file in fill_files:
        assert fill_file in expected_fill
        with open(os.path.join(path, fill_file), 'r') as reader:
            file_num = int(regex.search(fill_file).group(2))
            assert reader.read() == f'spam00{(file_num * 2) - 1}'

    # removes dir and it's contents (to ensure consistent test results)
    shutil.rmtree(path)
