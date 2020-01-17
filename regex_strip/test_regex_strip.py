from regex_strip import regex_strip

default_cases = ['      test       ',
                 '\nsample',
                 '\ttext',
                 '\n\twhitespace\n\t']

custom_cases = [('123test123', '123'),
                ('abcobfuscateabc', 'abc'),
                ('sampleEXAMPLEsample', 'sample'),
                ('123home123home123', '123'),
                ('123123home123home123123', '123')]


def test_regex_strip():
    for text in default_cases:
        assert regex_strip.regex_strip(text) == text.strip()

    for text, remove in custom_cases:
        assert regex_strip.regex_strip(text, remove) == text.strip(remove)
