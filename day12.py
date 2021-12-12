from day05 import read_input


def is_lower(character: str):
    return character == character.lower()


def is_done(paths_set):
    for v in paths_set:
        if v[-1] != 'end':
            return False
    return True


def update_paths(paths_set, to_append_set, current_path):
    for item in to_append_set:
        paths_set = paths_set - {current_path}
        earlier_path = list(current_path)
        if is_lower(item):
            if item not in earlier_path:
                paths_set.add(tuple(earlier_path + [item]))
        else:
            paths_set.add(tuple(earlier_path + [item]))
    return paths_set


def following_chars(input):
    d = {}
    for a, b in input:
        d[a] = []
        d[b] = []
    for a, b in input:
        d[a].append(b)
        d[b].append(a)
    return d


def find_paths_num(following_chars_dict, current_path, visited):
    if current_path[-1] == 'end':
        return 1
    available = following_chars_dict.get(current_path[-1], [])
    if not available:
        return 0
    if current_path[-1] in visited:
        return 0
    visited = visited | {current_path[-1]} if is_lower(current_path[-1]) else visited
    return sum([find_paths_num(following_chars_dict, current_path + [x], visited) for x in available])


def find_paths_num_part_2(following_chars_dict, current_path, visited, anyone_visited_twice):
    if current_path[-1] == 'start' and len(current_path) > 1:
        return 0
    if current_path[-1] == 'end':
        return 1
    available = following_chars_dict.get(current_path[-1], [])
    if not available:
        return 0
    if anyone_visited_twice and current_path[-1] in visited:
        return 0

    if is_lower(current_path[-1]):
        if anyone_visited_twice or current_path[-1] in visited:
            anyone_visited_twice = True

        visited = visited | {current_path[-1]} if is_lower(current_path[-1]) else visited

    return sum([find_paths_num_part_2(following_chars_dict, current_path + [x], visited, anyone_visited_twice) for x in
                available])


if __name__ == '__main__':
    data = [x.split('-') for x in read_input('input12.txt')]
    following_chars_d = following_chars(data)
    res1 = find_paths_num(following_chars_d, ['start'], set())
    res1_alternative = find_paths_num_part_2(following_chars_d, ['start'], set(), True)
    res2 = find_paths_num_part_2(following_chars_d, ['start'], set(), False)
    print(res1)
    print(res1_alternative)
    print(res2)
