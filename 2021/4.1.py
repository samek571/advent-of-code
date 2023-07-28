moves = open("input4.txt").read().strip().split("\n")
moves.pop()


def fx(moves):
    allboards = []

    # lottery
    drawns = ''.join(moves[0]).split(",")
    for i in range(len(drawns)):
        drawns[i] = int(drawns[i])

    # all bingos nicely ordered
    temp = []
    for i in moves[2:]:
        if i == "":
            allboards.append(temp)
            temp = []
            continue

        bingo_line = "".join(i).split()
        for u in range(5):
            bingo_line[u] = int(bingo_line[u])
        temp.append(bingo_line)

    match = Winning(drawns, allboards)
    sumaz = 0

    for i in match[0]:
        for j in i:
            if str(j).isnumeric() == True: sumaz += j

    sumaz *= 39
    return sumaz


def Winning(drawns, allboards):
    winner = []
    for chosen_number in drawns:

        for board in allboards:
            for line in board:

                # replacement
                for idx in range(5):
                    if line[idx] == chosen_number:
                        # print(line)
                        line[idx] = "x"
                        # print(line)

                        if line == ["x"] * 5:
                            winner.append(board)
                            print(chosen_number)
                            return winner

                # here was supposed to be some cycle that would check if bingo inst in column
                # however i want waste time if i can check just rows first


print(fx(moves))