import math
import re

from day05 import read_input


def add(a: str, b: str) -> str:
    num = '[' + a + ',' + b + ']'
    do_explosion, do_split = True, (True, '')
    while do_explosion or do_split[0]:
        do_explosion, do_split = get_exploding_pair(num), split_number(num)
        if do_explosion:
            num = explode(do_explosion[1], do_explosion[0], num)
        elif do_split[0]:
            num = do_split[1]
    return num


def get_exploding_pair(number: str) -> ((int), str):
    open_parenthesis = 0
    i = 0
    while i < len(number) and open_parenthesis != 5:
        if number[i] == '[':
            open_parenthesis += 1
        elif number[i] == ']':
            open_parenthesis -= 1
        i += 1

    if open_parenthesis == 5:
        pair = re.search(r'\d+,\d+', number[i - 1:])
        return (i + pair.span()[0] - 2, i + pair.span()[1] - 1), '[' + pair.group() + ']'
    return None


def explode(pair: str, pair_indices: (int), nested: str) -> str:
    new_nested = nested
    move_ind = False
    left_part = nested[:pair_indices[0]]
    nums_left = list(re.finditer(r'\d+', left_part))
    if nums_left:
        p = re.search(r'\d+', pair).group()
        if len(nums_left[-1].group()) > 1:
            to_add = left_part[nums_left[-1].span()[0]:nums_left[-1].span()[1]]
        else:
            to_add = left_part[nums_left[-1].span()[0]]

        adding = str(int(p) + int(to_add))

        if len(adding) > 1:
            move_ind = True
            ext = 1 if len(to_add) < 2 else 0
            pair_indices = (pair_indices[0] + ext, pair_indices[1] + 1)
        left_part = left_part[:nums_left[-1].span()[0]] + re.sub(to_add, adding, left_part[nums_left[-1].span()[0]:], 1)
        new_nested = left_part + new_nested[pair_indices[0]:]

    right_part = new_nested[pair_indices[-1] + 1:]
    nums_right = list(re.finditer(r'\d+', right_part))
    if nums_right:
        to_add = right_part[nums_right[0].span()[0]:nums_right[0].span()[1]]
        p = re.findall(r'\d+', pair)
        if len(nums_right[0].group()) == 1:
            to_add = right_part[nums_right[0].span()[0]]
        adding = str(int(p[-1]) + int(to_add))
        right_part = re.sub(to_add, adding, right_part, 1)
        new_nested = new_nested[:pair_indices[-1] + 1] + right_part
    if move_ind:
        new_nested = new_nested[:pair_indices[0]] + '0' + new_nested[pair_indices[-1]:]
    else:
        new_nested = new_nested[:pair_indices[0]] + '0' + new_nested[pair_indices[-1] + 1:]
    return new_nested


def split_number(number: str) -> (bool, str):
    n = re.search(r'\d{2}', number)
    if n:
        new_num = f'[{int(n.group()) // 2},{math.ceil(int(n.group()) / 2)}]'
        new_number = re.sub(r'\d{2}', new_num, number, 1)
        return True, new_number
    return False, number


def reduce_num(input_data: str) -> str:
    num = input_data[0]
    for i in range(1, len(input_data)):
        num = add(num, input_data[i])
    return num


def get_pair_magnitute(pair: re.Match) -> str:
    r = re.findall(r'\d+', pair.group())
    return str(int(r[0]) * 3 + int(r[1]) * 2)


def final_magnitude(numbers_str: str) -> int:
    if numbers_str.isalnum():
        return int(numbers_str)
    return final_magnitude(re.sub(r'\[\d+,\d+\]', get_pair_magnitute, numbers_str))


def get_largest_magnitude(input_numbers: str) -> int:
    magnitudes = [(final_magnitude(add(a, b))) for a in input_numbers for b in input_numbers]
    return max(magnitudes)


if __name__ == '__main__':
    data = read_input('input18.txt')
    part_1 = final_magnitude(reduce_num(data))
    print(part_1)

    part_2 = get_largest_magnitude(data)
    print(part_2)
