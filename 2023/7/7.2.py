import collections

def ordnung_muss_sein(hsh):
    jokers = 0 if 'J' not in hsh else hsh['J']
    if 'J' in hsh: del hsh['J']

    distinct_cards = len(hsh.values())

    if jokers >=4: return 7

    elif jokers == 3:
        #xyJJJ four of a kind
        if distinct_cards == 2: return 6
        #xxJJJ five of a kind
        elif distinct_cards == 1: return 7

    elif jokers == 2:
        #xyzJJ three of a kind
        if distinct_cards == 3: return 4
        #xxyJJ four of a kind
        elif distinct_cards == 2: return 6
        #xxxJJ five of a kind
        elif distinct_cards == 1: return 7

    elif jokers == 1:
        #xyzwJ one pair
        if distinct_cards == 4: return 2
        #xyzzJ three of a kind
        elif distinct_cards == 3: return 4
        #xxyyJ or xxxyJ
        elif distinct_cards == 2:
            #xxxyJ four of a kind
            if max(hsh.values()) == 3: return 6
            #xxyyJ fullhouse
            elif max(hsh.values())==2: return 5
        #xxxxJ
        elif distinct_cards == 1: return 7
    
    else: #jokers == 0
        #xyzwq High card
        if distinct_cards == 5: return 1
        #xxyzw one pair
        elif distinct_cards == 4: return 2
        #xxxxx five of a kind
        elif distinct_cards == 1: return 7

        #xxxyy or xxxxy four kind & fullhouse
        elif distinct_cards == 2:
            return 6 if max(hsh.values()) == 4 else 5

        #xxxyz or xxyyz three kind & two pair
        elif distinct_cards == 3:
            return 4 if max(hsh.values()) == 3 else 3


def fx(s):
    convert = {'J':1, **{str(i): i for i in range(2, 10)}, **{['T', 'Q', 'K', 'A'][i]: 10 + i for i in range(4)}}

    res = []
    for line in open(s).read().split("\n")[:-1]:
        hand, bet = line.split()
        res.append((ordnung_muss_sein(collections.Counter(hand)), *[convert[i] for i in hand], int(bet)))

    res = sorted(res, key=lambda x: x)
    return sum(res[i-1][-1] * i for i in range(1, len(res)+1))


print(fx('input7.txt'))
# too high 250606082
# too low  249628373
# too ok   250087440