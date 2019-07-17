import re
from pathlib import Path

from regex_search import regex_search


def test_regex_search():
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)

    matches = regex_search.regex_search(phone_regex, Path('./regex_search/sample_data/'))

    assert len(matches) == 3
    assert 'Phone: 987-654-3210' in matches
    assert 'ph: 555-555-5555' in matches
    assert 'phone: 444-444-4444' in matches
