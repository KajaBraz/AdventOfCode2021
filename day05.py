import re


def read_input(path: str) -> [str]:
    with open(path) as f:
        input_lines = [line.strip() for line in f]
    return input_lines


def create_board(coordinates: [int]):
    max_coord = max([max(pair) for pair in coordinates])
    return [[0 for i in range(max_coord + 1)] for y in range(max_coord + 1)]


def mark_points(coordinates: [int], board: [[int]], diagonals=False):
    for p in coordinates:
        x1 = p[0]
        y1 = p[1]
        x2 = p[2]
        y2 = p[3]

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                board[i][x1] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                board[y1][i] += 1
        else:
            if diagonals:
                x_sign = 1 if x2 > x1 else -1
                y_sign = 1 if y2 > y1 else -1
                for i, j in zip(range(x1, x2 + x_sign, x_sign), range(y1, y2 + y_sign, y_sign)):
                    board[j][i] += 1
    return board


def count_overlaps(marked_board: [[int]]) -> int:
    overlaps = 0
    for row in marked_board:
        overlaps += len([k for k in row if k > 1])
    return overlaps


if __name__ == '__main__':
    data = read_input('input05.txt')
    coord = [[int(x) for x in re.findall(r'\d*', row) if len(x) > 0] for row in data]

    board_part_1 = create_board(coord)
    board_part_2 = create_board(coord)
    board_with_points_part_1 = mark_points(coord, board_part_1)
    board_with_points_part_2 = mark_points(coord, board_part_2, True)
    res_1 = count_overlaps(board_with_points_part_1)
    res_2 = count_overlaps(board_with_points_part_2)
    print(res_1, res_2)
