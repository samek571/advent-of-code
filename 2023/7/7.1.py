import collections

def ordnung_muss_sein(hand, hsh):
    distinct_cards = len(hsh.values())
    # xyzwq High card
    if distinct_cards == 5:
        return 1
    # xxyzw one pair
    elif distinct_cards == 4:
        return 2
    # xxxxx five of a kind
    elif distinct_cards == 1:
        return 7

    # xxxyy or xxxxy four kind & fullhouse
    elif distinct_cards == 2:
        return 6 if max(hsh.values()) == 4 else 5

    # xxxyz or xxyyz three kind & two pair
    elif distinct_cards == 3:
        return 4 if max(hsh.values()) == 3 else 3



def fx(s):
    convert = {**{str(i): i for i in range(2, 10)}, **{['T', 'J', 'Q', 'K', 'A'][i]: 10 + i for i in range(5)}}

    res = []
    for line in open(s).read().split("\n")[:-1]:
        hand, bet = line.split()
        res.append((ordnung_muss_sein(hand, collections.Counter(hand)), *[convert[i] for i in hand], int(bet)))

    res = sorted(res, key=lambda x: x)
    return sum(res[i-1][-1] * i for i in range(1, len(res)+1))


print(fx('input7.txt'))
#250254244