from day05 import read_input


def adjust_input(input):
    return [[int(n) for n in line] for line in input]


def get_neighbours(board, current_ind):
    x, y = current_ind[0], current_ind[1]

    potential = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                 (x - 1, y - 1)]
    return [(neighbour_x, neighbour_y) for neighbour_x, neighbour_y in potential if
            0 <= neighbour_x < len(board) and 0 <= neighbour_y < len(board[x])]


def flash(point, board):
    neighbours = get_neighbours(board, point)
    for x, y in neighbours:
        board[x][y] += 1
    return board


def adjust_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 9:
                board[i][j] = 0
    return board


def reset(points_set, board):
    for x, y in points_set:
        board[x][y] = 0
    return board


def are_simultaneous(board):
    nums = [val for row in board for val in row]
    return sum(nums)


def step(board, n_flash):
    to_del_val = set()
    will_flash = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 9 and (i, j):
                will_flash.add((i, j))

    while will_flash:
        elem = will_flash.pop()
        board = flash(elem, board)
        n_flash += 1
        to_del_val.add(elem)
        for neigh in get_neighbours(board, elem):
            if board[neigh[0]][neigh[1]] >= 9 and neigh not in to_del_val:
                will_flash.add(neigh)

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += 1

    reset(to_del_val, board)
    return board, n_flash


def run(n_steps, board):
    n_flashes = 0
    for _ in range(n_steps):
        board, n_flashes = step(board, n_flashes)
    return board, n_flashes


def run2(board):
    n_step, n_flash = 0, 0
    while are_simultaneous(board) != 0:
        board, n_flash = step(board, n_flash)
        n_step += 1
    return n_step


if __name__ == '__main__':
    part_1 = run(100, adjust_input(read_input('input11.txt')))
    print(part_1[1])
    print(run2(adjust_input(read_input('input11.txt'))))
