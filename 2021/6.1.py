moves=open("input6.txt").read().split(",")
moves[-1]=moves[-1][:1]

for i in range(len(moves)):
    moves[i]=int(moves[i])


def fx(moves):
    day=1
    while day!=81:
        for fishidx in range(len(moves)):
            if moves[fishidx] == 0:
                moves[fishidx]=6
                moves.append(8)
            else: moves[fishidx]-=1

        day+=1
        print(day)

    return len(moves)


print(fx(moves))
# too low 339731