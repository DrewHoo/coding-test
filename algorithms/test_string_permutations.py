import tempfile
import os

from string_permutations import find_nth_permutation, find_permutations, \
    get_and_format_lines, convert_row_to_index_and_recalculate_row


def test_convert_row_to_index_and_recalculate_row():
    index, row = convert_row_to_index_and_recalculate_row(0, list('abcd'))
    expected_index = 0
    expected_row = 0
    assert (index, row) == (expected_index, expected_row)
    
    index, row = convert_row_to_index_and_recalculate_row(13, list('abcd'))
    expected_index = 2
    expected_row = 1
    assert (index, row) == (expected_index, expected_row)

    index, row = convert_row_to_index_and_recalculate_row(17, list('abcd'))
    expected_index = 2
    expected_row = 5
    assert (index, row) == (expected_index, expected_row)

    index, row = convert_row_to_index_and_recalculate_row(23, list('abcd'))
    expected_index = 3
    expected_row = 5
    assert (index, row) == (expected_index, expected_row)


def test_find_nth_permutation():
    permutation = find_nth_permutation(23, list('abcd'))
    assert permutation == 'dcba'

    permutation = find_nth_permutation(0, list('a'))
    assert permutation == 'a'

    permutation = find_nth_permutation(5, list('1Aa'))
    assert permutation == 'aA1'


def test_find_permutations():
    permutations = find_permutations(list('abc'))
    assert permutations == 'abc,acb,bac,bca,cab,cba'

    permutations = find_permutations(list('a'))
    assert permutations == 'a'

    permutations = find_permutations(list('12'))
    assert permutations == '12,21'


def test_get_and_format_lines():
    file = tempfile.NamedTemporaryFile()
    file.write(b'abc\n123')
    file.flush()
    chars_list = get_and_format_lines(file.name)
    file.close()
    assert chars_list[0] == ['a', 'b', 'c']
    assert chars_list[1] == ['1', '2', '3']
