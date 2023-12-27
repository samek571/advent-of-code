import re


def inputting(s):
    matrix=open(s).read().split("\n")
    matrix.pop()
    return matrix


def fx(s):
    ok = 0
    for line in s:
        oracle = {
            'r':0,
            'g':0,
            'b':0
        }

        line = line.replace(":", ";")
        line = line.split(';')

        for cases in line[1:]:
            cases = re.findall('[0-9]* [a-z]', cases)
            for subcase in cases:
                num, color = subcase.split(' ')
                oracle[color] = max(oracle[color], int(num))

        ok += oracle['r'] * oracle['b'] * oracle['g']

    return ok

print(fx(inputting('input2.txt')))