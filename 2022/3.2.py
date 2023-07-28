from collections import Counter

def inputting():
    moves=open("input3.txt").read().split("\n")
    moves.pop()
    return moves

def val(i):
    if i.isupper(): return ord(i)-38
    else: return ord(i)-96


def fx():
    moves = inputting()
    cnt = 0

    for rugidx in range(0, len(moves), 3):
        a, b, c = moves[rugidx], moves[rugidx+1], moves[rugidx+2]

        cmn = None
        for i in a:
            if i in b and i in c:
                cmn = i
                break

        cnt+= val(i)

    return cnt

print(fx())