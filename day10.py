from day05 import read_input


def is_correct(input_data: [str]) -> (bool, str):
    valid_brackets_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    opening_brackets = []
    for char in input_data:
        if char in valid_brackets_pairs:
            opening_brackets.append(char)
        else:
            if opening_brackets and char != valid_brackets_pairs[opening_brackets[-1]]:
                return False, char
            opening_brackets = opening_brackets[:-1]
    return True, ''


def count_score_corrupted(possible_corrupted: [(bool, str)]) -> int:
    scores = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137}
    final_score = 0
    for char in possible_corrupted:
        if not char[0]:
            final_score += scores[char[1]]
    return final_score


def filter_corrupted(input_lines: [str]) -> [str]:
    return [line for line in input_lines if is_correct(line)[0]]


def is_incomplete(filtered_line: str) -> (bool, [str]):
    valid_brackets_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    opening_brackets = []

    for bracket in filtered_line:
        if bracket in valid_brackets_pairs:
            opening_brackets.append(bracket)
        elif opening_brackets and bracket == valid_brackets_pairs[opening_brackets[-1]]:
            opening_brackets = opening_brackets[:-1]

    if opening_brackets:
        return True, complete_missing_brackets(opening_brackets)
    return False, []


def complete_missing_brackets(open_brackets: [str]) -> [str]:
    valid_brackets_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    return [valid_brackets_pairs[bracket] for bracket in open_brackets][::-1]


def count_score_incomplete(missing_part: [str]) -> int:
    scores = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4}
    score = 0
    for char in missing_part:
        score = score * 5 + scores[char]
    return score


if __name__ == '__main__':
    data = read_input('input10.txt')
    res1 = [is_correct(line) for line in data]
    print(count_score_corrupted(res1))

    filtered = filter_corrupted(data)
    res2 = [is_incomplete(line) for line in filtered]
    scores2 = [count_score_incomplete(line[1]) for line in res2]
    print(sorted(scores2)[len(scores2) // 2])
