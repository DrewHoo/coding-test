import sys
import math

from functools import reduce


def find_nth_permutation(row, chars):
    if len(chars) == 0:
        return ''

    index, row = convert_row_to_index_and_recalculate_row(row, chars)
    
    return chars[index] + find_nth_permutation(row, chars[:index] + chars[index + 1:])


def convert_row_to_index_and_recalculate_row(row, chars):
    width = len(chars)
    height = math.factorial(width)
    index = math.floor(row / height * width)

    block_height = height / width
    row -= int(index * block_height)
    return index, row


def find_permutations(chars):
    permutations = []
    for row in range(math.factorial(len(chars))):
        permutations.append(find_nth_permutation(row, chars[:]))
    return ','.join(permutations)


def get_and_format_lines(filename):
    with open(filename) as file:
        chars_list = [sorted(list(line.rstrip())) for line in file]
        return chars_list


if __name__ == '__main__':
    for chars in get_and_format_lines(sys.argv[1]):
        print(find_permutations(chars))
