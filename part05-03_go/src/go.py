# Write your solution here


def who_won(game_board: list):
    p1count = 0
    p2count = 0

    for item in game_board:
        for number in item:
            if number == 1:
                p1count += 1
            elif number == 2:
                p2count += 1
            else:
                continue

    if p1count > p2count:
        return 1
    elif p2count > p1count:
        return 2
    else:
        return 0

    


