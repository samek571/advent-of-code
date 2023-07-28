def inputting():
    moves=open("input2.txt").read().split("\n")
    moves.pop()
    return moves

def fx():
    moves = inputting()

    ttl=0
    default = {"X":1, "Y":2, "Z":3}


    for plays in moves:
        a,b= plays.split()

        if a == "A" and b == "X": ttl+=3+default[b]
        if a == "B" and b == "Y": ttl+=3+default[b]
        if a == "C" and b == "Z": ttl+=3+default[b]

        if a == "B" and b == "X": ttl+=default[b]
        if a == "C" and b == "Y": ttl+=default[b]
        if a == "A" and b == "Z": ttl+=default[b]

        if a == "A" and b == "Y": ttl+=6+default[b]
        if a == "B" and b == "Z": ttl+=6+default[b]
        if a == "C" and b == "X": ttl+=6+default[b]


    return ttl

print(fx())