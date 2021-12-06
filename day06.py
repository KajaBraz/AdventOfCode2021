from collections import Counter, defaultdict


def read_numeric_file(path: str) -> [int]:
    with open(path) as f:
        numbers = [int(number) for numbers in f for number in numbers.split(',')]
    return numbers


def simulate_lanternfish(input_data: [int], n_days: int) -> dict:
    counts = Counter(input_data)
    for _ in range(n_days):
        updated_counts = defaultdict(int)
        for lanternfish_state, lanternfish_num in counts.items():
            if lanternfish_state == 0:
                updated_counts[6] += lanternfish_num
                updated_counts[8] += lanternfish_num
            else:
                updated_counts[lanternfish_state - 1] += lanternfish_num
        counts = updated_counts
    return counts


def count_lanternfish(lanternfish_dict: {int: int}) -> int:
    return sum(lanternfish_dict.values())


if __name__ == '__main__':
    states = read_numeric_file('input06.txt')
    days_part_1 = 256
    days_part_2 = 80
    lanternfish_part_1 = simulate_lanternfish(states, days_part_1)
    lanternfish_part_2 = simulate_lanternfish(states, days_part_2)
    lanternfish_number_part_1 = count_lanternfish(lanternfish_part_1)
    lanternfish_number_part_2 = count_lanternfish(lanternfish_part_2)
    print(lanternfish_number_part_1)
    print(lanternfish_number_part_2)
