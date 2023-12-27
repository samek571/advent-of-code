import collections
import re

def fx(s):
    res=collections.defaultdict(int)
    for line in open(s).read().split("\n")[:-1]:
        winning, guessed = line.split("|")

        card_number = list(map(int, re.findall('[0-9]+', winning[:winning.index(":")])))[0]
        winning = set(map(int, re.findall('[0-9]+', winning[winning.index(":"):])))
        guessed = set(map(int, re.findall('[0-9]+', guessed)))

        res[card_number]+=1
        for i in range(1, len(winning & guessed)+1):
            res[card_number+i] += res[card_number]

    return sum(res.values())

print(fx('input4.txt'))
