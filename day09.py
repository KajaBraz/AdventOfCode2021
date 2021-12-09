from day05 import read_input


def get_neighbours(board, current_ind):
    x, y = current_ind[0], current_ind[1]

    if x == 0 and y == 0:
        return (x + 1, y), (x, y + 1)
    if x == len(board) - 1 and y == 0:
        return (x, y + 1), (x - 1, y)
    if x == 0 and y == len(board[x]) - 1:
        return (x + 1, y), (x, y - 1)
    if x == len(board) - 1 and y == len(board[x]) - 1:
        return (x - 1, y), (x, y - 1)
    if x == 0 and 0 < y < len(board[x]) - 1:
        return (x + 1, y), (x, y + 1), (x, y - 1)
    if len(board) - 1 > x > 0 == y:
        return (x + 1, y), (x, y + 1), (x - 1, y)
    if 0 < x < len(board) - 1 and y == len(board[x]) - 1:
        return (x + 1, y), (x - 1, y), (x, y - 1)
    if x == len(board) - 1 and 0 < y < len(board[x]) - 1:
        return (x - 1, y), (x, y - 1), (x, y + 1)

    return (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)


def is_low_point(board, point, neighbours):
    x, y = point[0], point[1]
    is_low = True
    for x_n, y_n in neighbours:
        if board[x][y] >= board[x_n][y_n]:
            is_low = False
    return is_low


def get_low_points(board):
    low_points = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbours = get_neighbours(board, (i, j))
            if is_low_point(board, (i, j), neighbours):
                low_points.append((board[i][j], (i, j)))
    return low_points


def find_basins(low_points, board):
    basins = []
    current_size = 1
    basin_points = set()
    next_neighbours = []
    for low_point in low_points:
        x, y = low_point[1]
        basin_points.add((x, y))
        neighbours = get_neighbours(board, (x, y))
        while neighbours:
            for neighbour in neighbours:
                x_n, y_n = neighbour[0], neighbour[1]
                if board[x_n][y_n] != '9' and (x_n, y_n) not in basin_points:
                    current_size += 1
                    next_neighbours.extend(get_neighbours(board, (x_n, y_n)))
                    basin_points.add((x_n, y_n))
            neighbours = next_neighbours
            next_neighbours = []

        basins.append(current_size)
        next_neighbours = []
        current_size = 1
        basin_points = set()
    return basins


if __name__ == '__main__':
    data = read_input('input09.txt')
    all_low_points = get_low_points(data)
    print(sum([int(s[0]) + 1 for s in all_low_points]))

    all_basins = sorted(find_basins(all_low_points, data), reverse=True)
    print(all_basins[0] * all_basins[1] * all_basins[2])
