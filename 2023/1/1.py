import re

def fx(s):
    res = 0
    for line in open(s).read().split("\n")[:-1]:
        dgts = re.findall('[0-9]', line)
        res += int(dgts[0] + dgts[-1])

    return res
print(fx('input1.txt'))