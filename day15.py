import heapq

from day05 import read_input


def get_paths_costs(board):
    costs = {(0, 0): 0}
    done = set()
    heap_costs = [(0, (0, 0))]
    while len(board) * len(board[0]) > len(done):
        current = heapq.heappop(heap_costs)
        neighs = get_neighbours(board, current[1])

        for neigh in neighs:
            neigh_curr_cost = board[neigh[0]][neigh[1]]
            if neigh in costs:
                neigh_prev_cost = costs[neigh]
                if neigh_prev_cost > current[0] + neigh_curr_cost:
                    costs[neigh] = current[0] + neigh_curr_cost
                    heapq.heappush(heap_costs, (costs[neigh], neigh))
            else:
                costs[neigh] = current[0] + neigh_curr_cost
                heapq.heappush(heap_costs, (costs[neigh], neigh))
        done.add(current[1])
    return costs[(len(board) - 1, len(board[-1]) - 1)]


def get_neighbours(board, coords):
    x, y = coords[0], coords[1]
    potential = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    return [(nx, ny) for nx, ny in potential if 0 <= nx < len(board) and 0 <= ny < len(board[x])]


def add_rightward(board_nums, vals, mul_factor):
    new_board = [[n for n in row] for row in board_nums]
    for _ in range(mul_factor - 1):
        next_step_board = [[vals[n] for n in row] for row in board_nums]
        for row in range(len(new_board)):
            new_board[row] += next_step_board[row]
        board_nums = next_step_board
    return new_board


def add_downward(board_nums, vals, mul_factor):
    new_board = [[n for n in row] for row in board_nums]
    for _ in range(mul_factor - 1):
        new_step_board = [[vals[n] for n in row] for row in board_nums]
        new_board += new_step_board
        board_nums = new_step_board
    return new_board


def multiply_board(board):
    vals = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 1}
    board_nums = [[int(n) for n in row] for row in board]
    widen_board = add_rightward(board_nums, vals, 5)
    new_board = add_downward(widen_board, vals, 5)
    return new_board


if __name__ == '__main__':
    input_board = read_input('input15.txt')

    # part 1
    data = [[int(num) for num in row] for row in input_board]
    data[0][0] = 0
    min_path_costs_p1 = get_paths_costs(data)
    print(min_path_costs_p1)

    # # part 2
    data = multiply_board(input_board)
    data[0][0] = 0

    min_path_costs_p2 = get_paths_costs(data)
    print(min_path_costs_p2)
