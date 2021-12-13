import re


def read_input(path: str) -> ({(int, int)}, [(str, int)]):
    point_pattern = re.compile(r'\d*,\d*')
    instrucrtions_pattern = re.compile(r'[xy]=\d*')
    points = set()
    with open(path) as f:
        s = f.read()
        pairs = point_pattern.findall(s)
        instructions = [i.split('=') for i in instrucrtions_pattern.findall(s)]
    pairs = [pair.split(',') for pair in pairs]
    points.update([(int(x), int(y)) for x, y in pairs])
    instructions = [(i[0], int(i[1])) for i in instructions]
    return points, instructions


def get_size(points: {(int, int)}) -> (int, int):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    return max_x, max_y


def get_board(input_points: {(int, int)}) -> [['']]:
    hor, vert = get_size(input_points)
    board = [['.' for i in range(hor + 1)] for j in range(vert + 1)]
    for x, y in input_points:
        board[y][x] = '#'
    return board


def draw_board(points: {(int, int)}) -> None:
    for row in points:
        print(row)


def fold_x(points: {(int, int)}, v: int) -> {(int, int)}:
    new_points = set()
    for x, y in points:
        if x > v:
            new_points.add((v - (x - v), y))
        else:
            new_points.add((x, y))
    return new_points


def fold_y(points: {(int, int)}, v: int) -> {(int, int)}:
    new_points = set()
    for x, y in points:
        if y > v:
            new_points.add((x, v - (y - v)))
        else:
            new_points.add((x, y))
    return new_points


def fold(points: {(int, int)}, instructions: [(str, int)]) -> [[str]]:
    for instruction in instructions:
        if instruction[0] == 'x':
            points = fold_x(points, instruction[1])
        else:
            points = fold_y(points, instruction[1])
    board = get_board(points)
    return board


if __name__ == '__main__':
    my_input_points, my_input_instructions = read_input('input13.txt')

    # part 1
    if my_input_instructions[0][0] == 'x':
        res = fold_x(my_input_points, my_input_instructions[0][1])
    else:
        res = fold_y(my_input_points, my_input_instructions[0][1])
    print(len(res))

    # part 2
    b = fold(my_input_points, my_input_instructions)
    draw_board(b)
