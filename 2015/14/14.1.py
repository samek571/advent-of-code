import re

def inputting():
    moves = open("input14.txt").read().split("\n")
    if not moves[-1]: moves.pop()

    new = []
    for i in moves:
        x= re.findall("\d+", i)
        new.append(x)

    return new


def fx(l):
    players = inputting()
    hashmap = dict()

    i=-1
    for tupec in players:
        i+=1
        v, t, chill = int(tupec[0]), int(tupec[1]), int(tupec[-1])


        hovno = l%(t+chill)
        tmp = 0
        if hovno >= t:
            tmp += v*t

        else:
            tmp += hovno*v/t

        hashmap[i] = t*v*(l//(t+chill)) + tmp

    return max(hashmap.values())



print(fx(1000))
print(fx(2503))