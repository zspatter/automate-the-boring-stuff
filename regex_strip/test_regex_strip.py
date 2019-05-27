from regex_strip import regex_strip

whitespace = ['      test       ', '\nsample', '\ttext', '\n\twhitespace\n\t']
custom = [('123test123', '123'), ('abcobfuscateabc', 'abc'), ('sampleEXAMPLEsample', 'sample')]


def test_regex_strip():
    for text in whitespace:
        assert regex_strip.regex_strip(text) == text.strip()

    for text, remove in custom:
        assert regex_strip.regex_strip(text, remove) == text.strip(remove)
