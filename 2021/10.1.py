import copy

def parsing():
    moves=open("input10.txt").read().split("\n")
    moves.pop()
    return moves

def fx():
    moves = parsing()
    copied_moves=copy.deepcopy(moves)

    point_counter=0
    points={")":3, "]":57, "}":1197, ">":25137}
    opened={"(","[","{","<"}
    pairs={("<",">"), ("(",")"), ("{","}"), ("[","]")}

    for line in moves:
        stack=[]
        washere=False
        for char in line:

            if char in opened: stack.append(char)
            elif (stack[-1],char) in pairs:
                stack.pop()
            else:
                washere=True
                point_counter+= points[char]
                break

        if washere == True:
            copied_moves.remove(line)

    return point_counter

print(fx())