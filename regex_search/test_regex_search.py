import re
from collections import Counter

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

    matches = regex_search.regex_search(phone_regex, './regex_search/sample_data/')
    counter = Counter(matches)

    assert counter['\n'] == 3
    assert '987-654-3210' in matches
    assert '555-555-5555' in matches
    assert '444-444-4444' in matches
