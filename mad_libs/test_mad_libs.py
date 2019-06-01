from mad_libs import mad_libs


def test_mad_libs(capsys):
    input_values = ['silly', 'chandelier', 'screamed', 'pickup truck']

    def mock_input(s):
        return input_values.pop(0)

    mad_libs.input = mock_input
    mad_libs.mad_libs('./mad_libs/sample_files/input.txt',
                      './mad_libs/sample_files/output.txt')

    with open('./mad_libs/sample_files/output.txt') as out:
        result = out.read()
        assert result == 'The silly panda walked to the chandelier and then screamed.' \
                         ' A nearby pickup truck was unaffected by these events.\n'
