from collections import Counter


def read_input(path: str) -> [str]:
    with open(path) as f:
        input_lines = [line.rstrip() for line in f]
    return input_lines


def get_vertical_numbers(str_numbers: [str]) -> [str]:
    return [''.join([str_numbers[i][j] for i in range(len(str_numbers))]) for j in range(len(str_numbers[0]))]


def get_gamma_and_oxygen(str_nums: [str]) -> (str, str):
    gamma_num, epsilon_num = '', ''
    for str_num in str_nums:
        bits = Counter(str_num)
        most_common = '1' if bits['1'] > bits['0'] else '0'
        least_common = '0' if most_common == '1' else '1'
        gamma_num += most_common
        epsilon_num += least_common
    return gamma_num, epsilon_num


def convert_binary_to_decimal(binary_num: str) -> int:
    return sum([int(n) * 2 ** (len(binary_num) - 1 - i) for i, n in enumerate(binary_num)])


def get_power_consumption(gamma_rate: int, epsilon_rate: int) -> int:
    return gamma_rate * epsilon_rate


def get_life_support_rating(oxygen_generator_rating: int, CO2_scrubber_rating: int) -> int:
    return oxygen_generator_rating * CO2_scrubber_rating


def find_oxygen_generator_rating(str_nums: [str], vertical_nums: [str]) -> str:
    vertical = vertical_nums
    nums = str_nums
    pos = 0
    while len(nums) != 1:
        bits = Counter(vertical[pos])
        most_common = '1' if bits['1'] >= bits['0'] else '0'
        nums = [num for num in nums if num[pos] == most_common]
        vertical = get_vertical_numbers(nums)
        pos += 1
    oxygen = nums[0]
    return oxygen


def find_CO2_scrubber_rating(str_nums: [str], vertical_nums: [str]) -> str:
    vertical = vertical_nums
    nums = str_nums
    pos = 0
    while len(nums) != 1:
        bits = Counter(vertical[pos])
        most_common = '1' if bits['1'] < bits['0'] else '0'
        nums = [num for num in nums if num[pos] == most_common]
        vertical = get_vertical_numbers(nums)
        pos += 1
    co2 = nums[0]
    return co2


if __name__ == '__main__':
    lines = read_input('input03.txt')
    vertical_numbers = get_vertical_numbers(lines)
    decimal_gamma_rate, decimal_epsilon_rate = [convert_binary_to_decimal(rate) for rate in
                                                get_gamma_and_oxygen(vertical_numbers)]
    sol_part_1 = get_power_consumption(decimal_gamma_rate, decimal_epsilon_rate)
    print(sol_part_1)
    decimal_oxygen_generator_rating = convert_binary_to_decimal(find_oxygen_generator_rating(lines, vertical_numbers))
    decimal_CO2_scrubber_rating = convert_binary_to_decimal(find_CO2_scrubber_rating(lines, vertical_numbers))
    sol_part_2 = get_life_support_rating(decimal_oxygen_generator_rating, decimal_CO2_scrubber_rating)
    print(sol_part_2)
