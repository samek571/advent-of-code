def inputting():
    moves=open("input1.txt").read().split("\n")
    moves.pop()
    return moves

def fx():
    moves = inputting()
    print(moves)

    output = []
    tmp = 0
    for ele in moves:
        if ele == '':
            output.append(tmp)
            tmp = 0

        else:
            tmp+=int(ele)
    output.append(tmp)

    output.sort(reverse=True)
    print(output)
    return output[0]+output[1]+output[2]

print(fx())