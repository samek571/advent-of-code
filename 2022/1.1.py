def inputting():
    moves=open("input1.txt").read().split("\n")
    moves.pop()
    return moves

def fx():
    moves = inputting()

    output = 0
    tmp = 0
    for ele in moves:
        if ele == '':
            output = max(output, tmp)
            tmp = 0

        else:
            tmp+=int(ele)
    return output

print(fx())