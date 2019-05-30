import os
import shutil

from selective_copy import selective_copy

expected_files = ('data.txt', 'input.txt', 'output.txt',
                  'requirements.txt', 'sample.txt', 'text.txt')


def test_selective_copy():
    output_path = './selective_copy/test_result/'

    # if output path exists, remove it prior to test
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    selective_copy.selective_copy('./selective_copy/search/', output_path, '.txt')
    output_path = os.path.abspath(output_path)

    assert len([name for name in os.listdir(output_path)
                if os.path.exists(os.path.join(output_path, name))]) == 6

    for file in expected_files:
        assert os.path.isfile(os.path.join(output_path, file))
