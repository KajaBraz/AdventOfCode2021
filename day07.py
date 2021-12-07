from day06 import read_numeric_file


def get_positions_and_displacements(possible_positions: [int], initial_positions: [int]) -> {int: [int]}:
    moves_dict = {}
    for p in possible_positions:
        updated_pos = [abs(pos - p) for pos in initial_positions]
        moves_dict[p] = updated_pos
    return moves_dict


def calculate_cost(moves_dict: {int: [int]}, inc=False) -> {int: int}:
    if not inc:
        return {position: sum(displacements) for position, displacements in moves_dict.items()}
    memo, moves_cost_dict = {}, {}
    for position, displacements in moves_dict.items():
        moves_cost_dict[position] = 0
        for displacement in displacements:
            if displacement not in memo:
                displacement_cost = sum([i + 1 for i in range(displacement)])
                memo[displacement] = displacement_cost
            else:
                displacement_cost = memo[displacement]
            moves_cost_dict[position] += displacement_cost
    return moves_cost_dict


def find_cheapest(moves_cost_dict: {int: int}):
    return min(moves_cost_dict.items(), key=lambda x: x[1])


if __name__ == '__main__':
    data = read_numeric_file('input07.txt')
    possible_final_positions = range(min(data), max(data))

    # PART I
    moves = get_positions_and_displacements(possible_final_positions, data)
    moves_cost = calculate_cost(moves)
    cheapest = find_cheapest(moves_cost)
    print(cheapest)

    # PART II
    moves = get_positions_and_displacements(possible_final_positions, data)
    moves_cost = calculate_cost(moves, True)
    cheapest = find_cheapest(moves_cost)
    print(cheapest)
