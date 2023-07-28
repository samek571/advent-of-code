def inputting():
    moves=open("input13.txt").read().split("\n")
    moves.pop()

    dick={}
    for i in moves:
        i = i.split(": ")
        dick[int(i[0])] = int(i[-1])

    return dick
print(inputting())

def fx():
    totalfuckingscore=0
    moves = inputting()
    for key, val in moves.items():
        if key % (2*(val-1)) == 0:
            totalfuckingscore += key*val

    return totalfuckingscore
print(fx())
