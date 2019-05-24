from comma_code import comma_code
from collections import Counter


def test_comma_code():
    empty_list = []
    single_item = ['cat']
    spam = ['apples', 'bananas', 'tofu', 'cats']
    mixed_list = [1, 2, 3.14, 'pi', 'avacado', True]

    empty_list_result = comma_code.comma_code(empty_list)
    single_item_result = comma_code.comma_code(single_item)
    spam_result = comma_code.comma_code(spam)
    mixed_list_result = comma_code.comma_code(mixed_list)

    assert empty_list_result == ''

    count = Counter(single_item_result)
    assert count[','] == 0
    assert single_item_result == str(single_item[0])

    count = Counter(spam_result)
    assert count[','] == (len(spam) - 1)
    assert ' and ' in spam_result
    for element in spam:
        assert str(element) in spam_result

    count = Counter(mixed_list_result)
    assert count[','] == (len(mixed_list) - 1)
    assert ' and ' in mixed_list_result
    for element in mixed_list:
        assert str(element) in mixed_list_result
