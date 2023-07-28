import copy


def inputting():
    moves = open("input24.txt").read().split("\n")
    moves.pop()

    matrix = []
    for i in moves:
        helper = []
        for char in i:
            helper.append(char)

        matrix.append(helper)

    return matrix


# print(inputting())

def finalcount(board):
    C = len(board)
    R = len(board[0])

    count = 0
    coef = 1
    for i in range(C):
        for j in range(R):
            if board[i][j] == "#": count += coef
            coef *= 2

    return count


# print(finalcount(inputting()))

def neigh(i, j, board):
    C = len(board)
    R = len(board[0])

    neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    number_of_bugs = 0
    for n in neighbors:
        if 0 <= i + n[0] < C and 0 <= j + n[1] < R:
            if board[i + n[0]][j + n[1]] == "#": number_of_bugs += 1

    if number_of_bugs != 1 and board[i][j] == "#":
        board[i][j] = "."
    elif board[i][j] == "." and number_of_bugs in {1, 2}:
        board[i][j] = "#"

    return board


def fx():
    occurences = []
    board = inputting()
    occurences.append(board)

    for y in board:
        print(y)

    C = len(board)
    R = len(board[0])
    while True:
        temp = copy.deepcopy(board)
        for i in range(C):
            for j in range(R):

                neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
                number_of_bugs = 0
                for n in neighbors:
                    if 0 <= i + n[0] < C and 0 <= j + n[1] < R:
                        if board[i + n[0]][j + n[1]] == "#": number_of_bugs += 1

                if number_of_bugs != 1 and board[i][j] == "#":
                    temp[i][j] = "."
                elif board[i][j] == "." and number_of_bugs in {1, 2}:
                    temp[i][j] = "#"

        print("")
        for y in temp:
            print(y)

        if temp in occurences: return finalcount(temp)
        board = temp
        occurences.append(temp)


print(fx())