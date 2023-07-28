'''
main contains
- set of visited by tail
- iterates via all the udlr instructions and
    --marks head pos, if abs(xyhead - xytail) is more than 2: tail gets prev head pos

'''

def inputting():
    moves=open("input9.txt").read().split("\n")
    moves.pop()
    return moves


def fxmain():
    x,y = 0, 0
    prev_head_pos, tail, seen = (x,y), (x,y), set()
    seen.add((x,y))
    hsh = {"R":(0,1), "L":(0,-1), "U":(-1, 0), "D":(1,0)}

    for instruction in inputting():
        print(instruction)


        vector = hsh[instruction[0]]
        for number_of_moves in range(int(instruction[2:])):
            prev_head_pos = (x,y)
            x, y = x+vector[0], y+vector[1]
            if abs(x-tail[0])>1 or abs(y-tail[1]) > 1:
                tail = prev_head_pos
                seen.add(tail)


    return len(seen)

print(fxmain())

