def get_data(path: str) -> [[int]]:
    input_data = [num.strip() for num in open(path, 'r').read().split('\n')]
    input_data = [[int(num) for num in row.split()] for row in input_data if len(row) > 0]
    return input_data


def check_bingo(board: [[int]]) -> bool:
    d = {}
    for i in range(len(board)):
        d[i] = [-1 for j in range(len(board[i])) if board[i][j] == -1]
    for k, v in d.items():
        if sum(v) == -5:
            return True
    return False


def transpose(board: [[int]]) -> [[int]]:
    return [[row[i] for row in board] for i in range(len(board))]


def sum_unmarked(board: [[int]]) -> int:
    return sum([sum(num for num in row if num != -1) for row in board])


def play_bingo(numbers: [int], boards: [[[int]]]) -> [([[int]], int)]:
    last_winner_dict = {board_id: board for board_id, board in enumerate(boards)}
    winner_boards = []
    for number in numbers:
        for board_id in range(len(boards)):
            if board_id in last_winner_dict:
                for row in boards[board_id]:
                    if number in row:
                        for x in range(len(row)):
                            if row[x] == number:
                                row[x] = -1
            res = check_bingo(boards[board_id])
            transposed_board = transpose(boards[board_id])
            res2 = check_bingo(transposed_board)
            if res or res2:
                if board_id in last_winner_dict:
                    winner_boards.append((last_winner_dict.pop(board_id), number))
    return winner_boards


def divide_in_boards(data):
    return [data[i * 5:i * 5 + 5] for i in range(len(data) // 5)]


if __name__ == '__main__':
    nums = '72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,' \
           '54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,' \
           '34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5 '
    nums = [int(n) for n in nums.split(',')]
    data = get_data('input04.txt')
    bingo_boards = divide_in_boards(data)

    winners = play_bingo(nums, bingo_boards)

    first_winner, at_number1 = winners[0][0], winners[0][1]
    sum_unmarked_nums1 = sum_unmarked(first_winner)
    print(sum_unmarked_nums1, at_number1)
    print(sum_unmarked_nums1 * at_number1)

    last_winner, at_number2 = winners[-1][0], winners[-1][1]
    sum_unmarked_nums2 = sum_unmarked(last_winner)
    print(sum_unmarked_nums2, at_number2)
    print(sum_unmarked_nums2 * at_number2)
