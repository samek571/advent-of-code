import collections
import re

def fx(s):
    res=0
    for line in open(s).read().split("\n")[:-1]:
        winning, guessed = line.split("|")

        winning = set(map(int, re.findall('[0-9]+', winning[winning.index(":"):])))
        guessed = set(map(int, re.findall('[0-9]+', guessed)))

        res+= 2**(len(winning & guessed)-1) if winning & guessed else 0

    return res

print(fx('input4.txt'))
