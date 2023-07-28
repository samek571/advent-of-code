import copy


def pre(depth, x,y):
    x, y= 1+x, 1+y
    matrix = [[0]*x for _ in range(y)]
    mod, matrix[0][0] =  20183, depth

    for line_idx in range(1, y): matrix[line_idx][0] = (depth + line_idx*48271)%mod
    for char_idx in range(1, x): matrix[0][char_idx] = (depth + char_idx*16807)%mod


    """erosion level at 0,y and x,0"""
    for line_idx in range(1, y):
        for char_idx in range(1, x):
            matrix[line_idx][char_idx] = (depth + matrix[line_idx][char_idx-1] * matrix[line_idx-1][char_idx])%mod
    matrix[y - 1][x - 1] = depth


    total = 0
    trans = {0: ".", 1:"=", 2:"|"}
    picogram = copy.deepcopy(matrix)
    for line_idx in range(y):
        for char_idx in range(x):
            picogram[line_idx][char_idx] = trans[matrix[line_idx][char_idx] % 3]
            matrix[line_idx][char_idx] = matrix[line_idx][char_idx]%3
        total += sum(matrix[line_idx])

    for i in matrix:
        print(i)
    for i in picogram:
        print("".join(i))

    return total


#print(pre(510, 10, 10))
print(pre(510, 10, 10))
#print(dp_final(510, 10, 10))
print(pre(7740, 12, 763)) # 9899
#too high 9947