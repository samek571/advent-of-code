import collections
from random import shuffle

'''little bit different approach has been chosen'''

s = "input19.txt"
data = [line.strip() for line in open(s)]
mol = data[-1]
oracle = []
for line in data[:-2]:
    tmp = line.split(" => ")
    oracle.append((tmp[0],tmp[-1]))


target = mol
res = 0

while target != 'e':
    tmp = target
    for a, b in oracle:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        res += 1

    if tmp == target:
        target = mol
        res = 0
        shuffle(oracle)

print(res)