from day05 import read_input


def move_east(board: [[str]]) -> ([[str]], bool):
    to_move = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '>' and board[i][(j + 1) % len(board[0])] == '.':
                to_move.add((i, j))
    new_board = [[item for item in row] for row in board]

    has_moved = True if len(to_move) > 0 else False

    for x, y in to_move:
        new_board[x][y] = '.'
        new_board[x][(y + 1) % len(new_board[0])] = '>'

    return new_board, has_moved


def move_south(board: [[str]], has_moved_east: bool) -> ([[str]], bool):
    to_move = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'v' and board[(i + 1) % len(board)][j] == '.':
                to_move.add((i, j))
    new_board = [[item for item in row] for row in board]
    has_moved = True if len(to_move) > 0 else False
    has_moved = has_moved or has_moved_east
    for x, y in to_move:
        new_board[x][y] = '.'
        new_board[(x + 1) % len(new_board)][y] = 'v'

    return new_board, has_moved


def move_cucumbers(input_data: [[str]]) -> ([[str]], bool):
    board = [[item for item in row] for row in input_data]
    steps, has_moved = 0, True
    while has_moved:
        board, has_moved = move_east(board)
        board, has_moved = move_south(board, has_moved)
        steps += 1
    return board, steps


if __name__ == '__main__':
    data = [[ch for ch in row] for row in read_input('input25.txt')]
    final_board, steps = move_cucumbers(data)
    print(steps)
