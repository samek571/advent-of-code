moves=open("input4.txt").read().strip().split("\n")
#moves.pop()

def fx(moves):
    allboards=[]

    #lottery
    drawns=''.join(moves[0]).split(",")
    for i in range(len(drawns)):
        drawns[i] = int(drawns[i])

    #all bingos nicely ordered
    temp=[]
    for i in moves[2:]:
        if i == "":
            allboards.append(temp)
            temp=[]
            continue

        bingo_line = "".join(i).split()
        for u in range(5):
            bingo_line[u] = int(bingo_line[u])
        temp.append(bingo_line)
    allboards.append(temp)


    match, chosen = Winning(drawns, allboards)
    print(chosen, match)
    sumaz=0
    for i in match:
        for j in i:
            if str(j).isnumeric() == True: sumaz+=j

    sumaz *= chosen
    return sumaz



def Winning(drawns, allboards):
    winners = []
    for chosen_number in drawns:
        print(chosen_number)
        for board in allboards:
            for line in board:

                #replacement
                for idx in range(len(line)):
                    if line[idx] == chosen_number:
                        line[idx] = "x"
                        break


                #checking rows
                if line == ["x"]*5:
                    winners.append(board)
                    allboards.remove(board)

                    if len(allboards)==1:
                        print("rows")
                        return winners[-1], chosen_number
                    break

            if board in allboards:
                #checking columns
                transponed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
                for line in transponed:
                    if line == ["x"]*5:
                        winners.append(board)
                        allboards.remove(board)
                        if len(allboards) == 0:
                            print("columns")
                            return winners[-1], chosen_number
                        else: break


print(fx(moves))
# 10692 too low, however the win has been coded just for the rows + error
# 18612 too low, however the win has been coded just for the rows
# 20066 too low
# 26486 :/
# 44226 :/
# 49842?
# 35530? just the rows