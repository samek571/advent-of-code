import copy

def part2(matrix):
    n, m = len(matrix), len(matrix[0])
    matrix[0][0] = "#"
    matrix[n-1][0] = "#"
    matrix[0][m-1] = "#"
    matrix[n-1][m-1] = "#"
    return matrix


def fx(matrix, iter_, part1):
    n, m, cnt = len(matrix), len(matrix[0]), 0

    while cnt != iter_:
        cnt+=1

        tmp = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(m):

                neighs = 0
                for a,b in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    x,y = i+a, j+b
                    if 0<=x<n and 0<=y<m:
                        if matrix[x][y] == "#":
                            neighs+=1

                if (matrix[i][j] == "#" and neighs in {2,3}) or (matrix[i][j] == "." and neighs == 3):
                    tmp[i][j] = "#"
                else: tmp[i][j] = "."

        matrix = copy.deepcopy(tmp)
        if not part1:
            matrix = part2(matrix)

        # for i in matrix:
        #     print(i)
        # print()


    res = 0
    for line in matrix:
        res += sum(1 for i in line if i == "#")

    return res



s = 'input18.txt'
matrix = [[i for i in line] for line in open(s).read().strip().split("\n")]
matrix = part2(matrix)

print(fx(matrix, 100, False))