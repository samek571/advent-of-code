number_of_time_rolled = 0
dice = 1
firstplayer_pos = 7
firstplayer_score = 0
secondplayer_pos = 5
secondplayer_score = 0

round = 0
while secondplayer_score < 1000 and firstplayer_score < 1000:

    one_move = 0
    for i in range(3):
        one_move += dice
        dice += 1
        dice %= 100
        number_of_time_rolled += 1

    # first player
    if round % 2 == 0:
        firstplayer_pos += one_move
        firstplayer_pos %= 10

        if firstplayer_pos == 0: firstplayer_pos = 10
        firstplayer_score += firstplayer_pos
        round += 1

    # second player
    else:
        secondplayer_pos += one_move
        secondplayer_pos %= 10

        if secondplayer_pos == 0: secondplayer_pos = 10
        secondplayer_score += secondplayer_pos
        round += 1

print(number_of_time_rolled * min(firstplayer_score, secondplayer_score))