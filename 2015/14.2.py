import collections
import re

def inputting():
    moves = open("input14.txt").read().split("\n")
    if not moves[-1]: moves.pop()

    new = []
    for i in moves:
        tmp=[]
        x= re.findall("\d+", i)

        for ele in x:
            tmp.append(int(ele))

        new.append(tmp)

    return new



def fx(l):
    players = inputting()
    n = len(players)

    leaderboard = {i:0 for i in range(n)}
    traveled = [0 for _ in range(n)]

    for sec in range(l):

        # move for each second and each player
        for idx, txn in enumerate(players):
            v, trav_time, chill_time = txn[0], txn[1], txn[-1]

            #<= or <
            if sec%(trav_time+chill_time) < trav_time:
                traveled[idx] = v + traveled[idx]

            # else kokotko sotji na mieste

        w = [idx for idx, value in enumerate(traveled) if value == max(traveled)]

        for i in w:
            leaderboard[i]+=1

    print(leaderboard.values())
    return max(leaderboard.values())


print(fx(1000))
print(fx(2503))