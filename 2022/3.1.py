from collections import Counter

def inputting():
    moves=open("input3.txt").read().split("\n")
    moves.pop()

    # for i in moves:
    #     if len(i)%2==1: return False

    return moves

def val(i):
    if i.isupper(): return ord(i)-38
    else: return ord(i)-96


def fx():
    moves = inputting()
    cnt = 0

    for rug in moves:
        n = len(rug)
        a, b = rug[:n//2], rug[n//2:]

        cmn = None
        for i in b:
            if i in a:
                cmn = i
                break

        cnt+= val(i)

    return cnt

print(fx())