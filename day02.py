def get_data(path: str) -> ([str], [int]):
    data = open(path, 'r').read().split()
    directions = [data[i] for i in range(len(data)) if i % 2 == 0]
    values = [int(data[i]) for i in range(len(data)) if i % 2 == 1]
    return directions, values


def calculate_position(directions: [str], values: [int]):
    horizontal_pos, depth = 0, 0
    for i in range(len(directions)):
        if directions[i] == 'forward':
            horizontal_pos += values[i]
        elif directions[i] == 'up':
            depth -= values[i]
        elif directions[i] == 'down':
            depth += values[i]
        else:
            horizontal_pos -= values[i]
    return horizontal_pos, depth, horizontal_pos * depth


def calculate_position_with_aim(directions: [str], values: [int]):
    h, d, aim = 0, 0, 0
    for i in range(len(directions)):
        if directions[i] == 'forward':
            h += values[i]
            d += aim * values[i]
        elif directions[i] == 'up':
            aim -= values[i]
        elif directions[i] == 'down':
            aim += values[i]
        else:
            h -= values[i]
    return h, d, h * d


if __name__ == '__main__':
    positions, vals = get_data('input02.txt')
    h_part1, d_part1, multiplied_part1 = calculate_position(positions, vals)
    print(h_part1, d_part1, multiplied_part1)
    h_part2, d_part2, multiplied_part2 = calculate_position_with_aim(positions, vals)
    print(h_part2, d_part2, multiplied_part2)
