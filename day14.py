from collections import defaultdict
from copy import copy


def parse_input(path):
    with open(path, 'r') as f:
        lines = f.read()
    input_rules = lines.split()
    start = input_rules[0]
    input_rules = {input_rules[a]: input_rules[a + 2] for a in range(1, len(input_rules) - 1) if (a - 1) % 3 == 0}
    return start, input_rules


def do_insertions(input_rules, start, n_step):
    adjacent = defaultdict(int)
    for i in range(len(start) - 1):
        adjacent[start[i:i + 2]] += 1

    for i in range(n_step):
        updated = copy(adjacent)
        for k, v in adjacent.items():
            insertion = input_rules[k]
            updated[k] -= v
            updated[k[0] + insertion] += v
            updated[insertion + k[1]] += v
        adjacent = updated

    single_counts = defaultdict(int)
    for k, v in adjacent.items():
        single_counts[k[0]] += v
    single_counts[start[-1]] += 1

    return single_counts


def find_most_least_common(pol):
    max_v = max(pol.values())
    min_v = min(pol.values())
    return max_v, min_v


if __name__ == '__main__':
    initial_polymer, rules = parse_input('input14.txt')

    most_least_common_after_10 = find_most_least_common(do_insertions(rules, initial_polymer, 10))
    part_1_res = most_least_common_after_10[0] - most_least_common_after_10[1]
    print(part_1_res)

    most_least_common_after_40 = find_most_least_common(do_insertions(rules, initial_polymer, 40))
    part_2_res = most_least_common_after_40[0] - most_least_common_after_40[1]
    print(part_2_res)
