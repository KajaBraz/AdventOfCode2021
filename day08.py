from day05 import read_input


def pipe_split(input_data):
    lines_split = [line.split() for line in input_data]
    return [(line[:10], line[11:]) for line in lines_split]


def count_unique_values(lines_output):
    unique_vials_lengths = {2: 1, 3: 7, 7: 8, 4: 4}
    lengths = [val for val in lines_output if len(val) in unique_vials_lengths]
    return len(lengths)


def get_single_values(line_output):
    all_nums_dict = set([''.join(sorted(num)) for num in line_output[0] + line_output[1]])
    return all_nums_dict


def get_unique_values(all_nums_set):
    all_line_nums = list(all_nums_set)
    d = {}
    unique_vials_lengths = {2: 1, 3: 7, 7: 8, 4: 4}
    for num in all_line_nums:
        if len(num) in unique_vials_lengths:
            d[num] = unique_vials_lengths[len(num)]
    return d


def get_common_edge(v1, v2):
    return set(v1) & set(v2)


def decode_line_numbers(line_nums):
    all_nums = get_single_values(line_nums)
    unique_values = get_unique_values(all_nums)
    unique_values_tr = {v: k for (k, v) in unique_values.items()}

    decoded = {}
    for val in all_nums:
        if val in unique_values:
            decoded[val] = unique_values[val]

        if len(val) == 5:
            if len(get_common_edge(val, unique_values_tr[1])) == 1:
                if len(get_common_edge(val, unique_values_tr[4])) == 2:
                    if len(get_common_edge(val, unique_values_tr[7])) == 2:
                        decoded[val] = 2

            if len(get_common_edge(val, unique_values_tr[1])) == 2:
                if len(get_common_edge(val, unique_values_tr[4])) == 3:
                    if len(get_common_edge(val, unique_values_tr[7])) == 3:
                        decoded[val] = 3

            if len(get_common_edge(val, unique_values_tr[1])) == 1:
                if len(get_common_edge(val, unique_values_tr[4])) == 3:
                    if len(get_common_edge(val, unique_values_tr[7])) == 2:
                        decoded[val] = 5
        elif len(val) == 6:
            if len(get_common_edge(val, unique_values_tr[1])) == 2:
                if len(get_common_edge(val, unique_values_tr[4])) == 3:
                    if len(get_common_edge(val, unique_values_tr[7])) == 3:
                        decoded[val] = 0
            if len(get_common_edge(val, unique_values_tr[1])) == 1:
                if len(get_common_edge(val, unique_values_tr[4])) == 3:
                    if len(get_common_edge(val, unique_values_tr[7])) == 2:
                        decoded[val] = 6

            if len(get_common_edge(val, unique_values_tr[1])) == 2:
                if len(get_common_edge(val, unique_values_tr[4])) == 4:
                    if len(get_common_edge(val, unique_values_tr[7])) == 3:
                        decoded[val] = 9

    return decoded


def get_decoded_output_val(encoded_output, decoded_nums):
    output_val = ''
    for encoded_num in encoded_output:
        sorted_num = ''.join(sorted(encoded_num))
        output_val += str(decoded_nums[sorted_num])
    return int(output_val)


if __name__ == '__main__':
    data = pipe_split(read_input('input08.txt'))
    only_output_values = [split_line[1] for split_line in data]
    unique_output_num = [count_unique_values(val) for val in only_output_values]
    part_1_sol = sum(unique_output_num)
    print(part_1_sol)

    output_values = []
    for split_line in data:
        decoded_dict = decode_line_numbers(split_line)
        output_values.append(get_decoded_output_val(split_line[1], decoded_dict))
    part_2_sol = sum(output_values)
    print(part_2_sol)
