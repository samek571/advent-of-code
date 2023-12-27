import re


def inputting(s):
    matrix=open(s).read().split("\n")
    matrix.pop()
    return matrix

oracle = {
    'r':12,
    'g':13,
    'b':14
}

def fx(s):
    ok = 0
    for line in s:
        line = line.replace(":", ";")
        line = line.split(';')

        impossible_situation = False
        for cases in line[1:]:
            if impossible_situation: break

            cases = re.findall('[0-9]* [a-z]', cases)
            for subcase in cases:
                num, color = subcase.split(' ')
                if oracle[color] < int(num) and not impossible_situation:
                    impossible_situation = True

        if not impossible_situation:
            ok+=int("".join(re.findall('[0-9]', line[0])))

    return  ok

print(fx(inputting('input2.txt')))