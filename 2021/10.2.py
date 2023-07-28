import copy

def parsing():
    moves=open("input10.txt").read().split("\n")
    moves.pop()
    return moves

def fx():
    moves = parsing()
    copied_moves=copy.deepcopy(moves)
    returnment=[]

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

        if washere == True: copied_moves.remove(line)
        else:
            returnment.append("".join(stack))

    return returnment

print(fx())

def second():
    moves = fx()
    output=[]
    points = {"<":4, "{":3, "(":1, "[":2}

    for line in moves:
        line = line[::-1]
        print(line)

        counter=0
        for char in line:
            counter *= 5
            counter += points[char]

        output.append(counter)

    output.sort()

    return output[len(output)//2]

print(second())
