import sys
from collections import defaultdict

from day05 import read_input


def get_paths(board, x, y, cur_risk):
    if x == len(board) - 1 and y == len(board[0]) - 1:
        return {cur_risk}
    if x == len(board) - 1:
        return get_paths(board, x, y + 1, cur_risk + board[x][y])
    if y == len(board[0]) - 1:
        return get_paths(board, x + 1, y, cur_risk + board[x][y])
    return get_paths(board, x, y + 1, cur_risk + board[x][y]) | get_paths(board, x + 1, y, cur_risk + board[x][y])


def get_paths3(board, x, y, cur_risk):
    if x == len(board) - 1 and y == len(board[0]) - 1:
        return cur_risk + board[x][y]
    if x == len(board) - 1:
        return get_paths3(board, x, y + 1, cur_risk + board[x][y])
    if y == len(board[0]) - 1:
        return get_paths3(board, x + 1, y, cur_risk + board[x][y])
    return min(get_paths3(board, x, y + 1, cur_risk + board[x][y]), get_paths3(board, x + 1, y, cur_risk + board[x][y]))


def get_paths4(board, x, y, cur_risk, visited):
    if (x, y) in visited:
        return cur_risk
    if x == len(board) - 1 and y == len(board[0]) - 1:
        return cur_risk

    neighs = [neighbour for neighbour in get_neighbours(board, (x, y)) if neighbour not in visited]
    if neighs:
        visited = visited | {(x, y)}
        return min([get_paths4(board, neigh[0], neigh[1], cur_risk + board[x][y], visited) for neigh in neighs])
    return 1000


def get_min(board, min_costs, x, y, visited):
    neighs = get_neighbours(board, (x, y))
    known_neighs = [neigh for neigh in neighs if neigh in visited]
    unknown_neighs = [neigh for neigh in neighs if neigh not in visited]
    return min(
        [min_costs[neigh] for neigh in known_neighs] + [get_min(board, min_costs, neigh[0], neigh[1], visited) for neigh
                                                        in unknown_neighs])


def get_paths_costs5(board):
    sys.setrecursionlimit(10000)
    visited = set()
    min_costs = {(0, 0): 0}
    for x in range(len(board)):
        for y in range(len(board[x])):
            min_costs[(x, y)] = get_min(board, min_costs, x, y, visited)
            visited.add((x, y))
    return min_costs[(len(board) - 1, len(board[-1]) - 1)]


def get_paths_costs(board):
    paths_costs_up_to_point = defaultdict(int)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0:
                paths_costs_up_to_point[(i, j)] = board[i][j] + paths_costs_up_to_point[(i, j - 1)]
            elif j == 0:
                paths_costs_up_to_point[(i, j)] = board[i][j] + paths_costs_up_to_point[(i - 1, j)]
            else:
                paths_costs_up_to_point[(i, j)] = min(board[i][j] + paths_costs_up_to_point[(i - 1, j)],
                                                      board[i][j] + paths_costs_up_to_point[(i, j - 1)])
    return paths_costs_up_to_point


def get_paths_costs3(board):
    costs = {(0, 0): 0}
    done = set()
    while len(board) * len(board[0]) > len(done):
        current = get_current_lowest_cost(costs, done)
        neighs = get_neighbours(board, current[0])
        for neigh in neighs:
            neigh_curr_cost = board[neigh[0]][neigh[1]]
            if neigh in costs:
                neigh_prev_cost = costs[(neigh[0], neigh[1])]
                if neigh_prev_cost > current[1] + neigh_curr_cost:
                    costs[(neigh[0], neigh[1])] = current[1] + neigh_curr_cost
            else:
                costs[(neigh[0], neigh[1])] = current[1] + neigh_curr_cost
        done.add(current[0])
    return costs[(len(board) - 1, len(board[-1]) - 1)]


def get_current_lowest_cost(costs, done):
    items = sorted(costs.items(), key=lambda x: x[1])
    for item in items:
        if item[0] not in done:
            return item
    return None


def get_lowest_cost(costs, board, nodes_list):
    return min([(board[node[0]][node[1]], node) for node in nodes_list], key=lambda x: x[0])


def find_lowest_cost_path(board, costs, start_coords, target_coords):
    visited = {(0, 0)}
    final_cost = 0
    x, y = start_coords
    if (x, y) == target_coords:
        return costs, target_coords

    neighbouring = [neighbour for neighbour in get_neighbours(board, (x, y)) if neighbour not in visited]

    while (x, y) != target_coords and neighbouring:
        neighbouring = [neighbour for neighbour in get_neighbours(board, (x, y)) if neighbour not in visited]
        if neighbouring:
            cheapest, coords = get_lowest_cost(costs, board, neighbouring)
            visited.add(coords)
            final_cost += cheapest
            x, y = coords
    return final_cost


def get_neighbours(board, coords):
    x, y = coords[0], coords[1]

    potential = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    return [(nx, ny) for nx, ny in potential if 0 <= nx < len(board) and 0 <= ny < len(board[x])]


if __name__ == '__main__':
    data = [[int(num) for num in row] for row in read_input('input15.txt')]
    data[0][0] = 0
    # data_dict = defaultdict()
    # for d in data:
    #     print(d)
    # data_dict[i] = data[i]
    # p = get_paths(data, 0, 0, 0)
    # print(p)
    # print(min(p))
    #
    # costs_up_to_the_point = defaultdict(int)
    # p_min = get_paths3(data, 0, 0, 0)
    # p_min = get_paths4(data, 0, 0, 0, set())
    # print(p_min)
    # data[0][0] = 0
    # min_path_costs = get_paths_costs(data, 0, 0, costs_up_to_the_point)
    # min_path_costs = get_paths_costs(data, 0, 0, (9, 9))
    min_path_costs = get_paths_costs3(data)
    # min_path_costs = get_paths_costs5(data)
    print(min_path_costs)
    # final_cost = find_lowest_cost_path(data, min_path_costs, (0, 0), (9, 9))
    # final_cost = find_lowest_cost_path(data,0,(0,0),(99,99))
    # print('final', final_cost)

    # print(get_lowest_cost(min_path_costs, get_neighbours(data, (2,2))))
