
def computering(matrix, bounty_fuckers):
    for line_idx in range(1, len(matrix)):
        fuckers = 0
        for j in range(min(line_idx, len(matrix) - line_idx)):
            fuckers += sum(a!=b for a, b in zip(matrix[line_idx - j - 1], matrix[line_idx + j]))

        if fuckers == bounty_fuckers:
            return line_idx

    return False


def fx(s):
    matrices = [shit.split("\n") for shit in open(s).read().strip().split("\n\n")]

    #could be a 1 liner...
    res1, res2 = 0, 0
    for matrix in matrices:
        #part 1
        res1 += 100*computering(matrix, 0) + computering([list(row) for row in zip(*matrix)], 0)

        #part 2
        res2 += 100*computering(matrix, 1) + computering([list(row) for row in zip(*matrix)], 1)

    return res1, res2

print(fx('input13.txt'))
