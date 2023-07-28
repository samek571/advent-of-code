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
    moves = inputting()
    for i in range(1, 100000000):

        totalfuckingscore=0
        for key, val in moves.items():

            if (key+i) % (2 * (val - 1))  == 0:
                totalfuckingscore += (key+i) * val
                break

        if totalfuckingscore==0:
            return i

print(fx())
