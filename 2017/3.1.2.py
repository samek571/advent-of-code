def checkneighb(matrix, i, j, k):
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    sumaz=matrix[i][j]
    for n in neighbors:
        if 0 <= i + n[0] < k and 0 <= j + n[1] < k:
            sumaz += matrix[i + n[0]][j + n[1]]

    matrix[i][j] = sumaz
    return matrix

def fx(k):
    matrix = [[0]*k for _ in range(k)]

    print("innit")
    for u in matrix:
        print(u)

    iteration=1
    howmany=1
    rotation=90
    i, j = k//2, k//2
    matrix[i][j] = 1
    while True:

        if rotation == 90:
            for x in range(howmany):
                j+=1
                matrix = checkneighb(matrix, i, j, k)
        rotation=0

        if rotation == 0:
            for x in range(howmany):
                i-=1
                matrix = checkneighb(matrix, i, j, k)
        rotation=270

        if rotation == 270:
            for x in range(howmany+1):
                j-=1
                matrix = checkneighb(matrix, i, j, k)
        rotation=180

        if rotation == 180:
            for x in range(howmany + 1):
                i+=1
                matrix = checkneighb(matrix, i, j, k)
        rotation = 90

        howmany+=2
        iteration+=1

        print(i, j)
        print("")
        for u in matrix:
            print(u)


        if matrix[i][j]>312051: break


print(fx(17))