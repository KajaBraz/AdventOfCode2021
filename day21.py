def turn(current_pos, current_points, last_roll):
    new_pos = (current_pos + last_roll * 3 + 1 + 2 + 3) % 10
    if new_pos == 0:
        new_pos = 10
    points = current_points + new_pos
    return new_pos, points


def already_won(game_points):
    for score in game_points:
        if score >= 1000:
            return True
    return False


def play(starting_pos_1, starting_pos_2):
    points = [0, 0]
    rolls = 0
    p1 = {'current_pos': starting_pos_1, 'points': 0}
    p2 = {'current_pos': starting_pos_2, 'points': 0}
    current_turn = 0
    while not already_won(points):
        if current_turn == 0:
            pos, score = turn(p1['current_pos'], p1['points'], rolls)
            p1['current_pos'] = pos
            p1['points'] = score
            points[0] = score
        else:
            pos, score = turn(p2['current_pos'], p2['points'], rolls)
            p2['current_pos'] = pos
            p2['points'] = score
            points[1] = score
        rolls += 3
        current_turn = (current_turn + 1) % 2
    return points, rolls


def play_multiversum(pos_1, pos_2, score_1, score_2, current_player, games):
    if score_1 >= 21:
        return 1, 0
    if score_2 >= 21:
        return 0, 1
    if (pos_1, pos_2, score_1, score_2, current_player) in games:
        return games[(pos_1, pos_2, score_1, score_2, current_player)]

    new_wins_1, new_wins_2 = 0, 0
    for dice_1 in range(1, 4):
        for dice_2 in range(1, 4):
            for dice_3 in range(1, 4):

                if current_player == 1:
                    new_pos_1 = (pos_1 + dice_1 + dice_2 + dice_3) % 10
                    if new_pos_1 == 0:
                        new_pos_1 = 10
                    new_score_1 = score_1 + new_pos_1
                    wins_1, wins_2 = play_multiversum(new_pos_1, pos_2, new_score_1, score_2, 2, games)
                    new_wins_1 += wins_1
                    new_wins_2 += wins_2

                else:
                    new_pos_2 = (pos_2 + dice_1 + dice_2 + dice_3) % 10
                    if new_pos_2 == 0:
                        new_pos_2 = 10
                    new_score_2 = score_2 + new_pos_2
                    wins_1, wins_2 = play_multiversum(pos_1, new_pos_2, score_1, new_score_2, 1, games)
                    new_wins_1 += wins_1
                    new_wins_2 += wins_2

    games[(pos_1, pos_2, score_1, score_2, current_player)] = (new_wins_1, new_wins_2)
    return new_wins_1, new_wins_2


if __name__ == '__main__':
    initial_position_1, initial_position_2 = 10, 8
    players_points, rolls_num = play(initial_position_1, initial_position_2)
    sol_part_1 = min(players_points) * rolls_num
    print(sol_part_1)

    winner_1, winner_2 = play_multiversum(initial_position_1, initial_position_2, 0, 0, 1, {})
    sol_part_2 = (max(winner_1, winner_2))
    print(sol_part_2)
