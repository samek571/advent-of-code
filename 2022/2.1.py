def inputting():
    moves=open("input2.txt").read().split("\n")
    moves.pop()
    return moves

def fx():
    moves = inputting()

    ttl=0

    loss= {"A":3 ,"B":1 ,"C":2}
    win = {"A":2, "B":3, "C":1}
    tie= {"A":1, "B":2, "C":3}

    fate= {"X":0, "Y":3, "Z":6}
    for plays in moves:
        a,b= plays.split()

        if b == "Y":
            ttl+=tie[a]+fate[b]

        elif b == "Z":
            ttl+=win[a]+fate[b]

        elif b == "X":
            ttl+=loss[a]+fate[b]




    return ttl

print(fx())