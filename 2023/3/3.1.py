import collections


def fx(s):
    matrix=[[char for char in line] for line in open(s).read().split("\n")[:-1]]

    m,n = len(matrix), len(matrix[0])
    res = 0

    for idx, line in enumerate(matrix):
        for jdx, char in enumerate(line):
            if char != "." and not char.isnumeric():

                for x,y, in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    i,j = x+idx,y+jdx
                    if 0<=i<m and 0<=j<n and matrix[i][j].isnumeric():
                        l,r = j-1,j
                        number=collections.deque()
                        while r<m and matrix[i][r].isnumeric():
                            number.append(matrix[i][r])
                            matrix[i][r] = "."
                            r+=1

                        while l>=0 and matrix[i][l].isnumeric():
                            number.appendleft(matrix[i][l])
                            matrix[i][l] = "."
                            l-=1

                        if number:
                            res+=int(''.join(number))

    return res

print(fx('input3.txt'))
# 521840 too low