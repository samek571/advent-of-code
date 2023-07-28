from collections import Counter

def parsing():
    moves=open("input14h.txt").read().split("\n")
    moves.pop()
    s=moves[0]
    insertions = {}

    for i in moves[2:]:
        first = i[0]+i[1]
        insertions[first] = i[-1]

    pairs = Counter()
    for i in range(len(s) - 1):
        pairs[s[i] + s[i + 1]] += 1

    return s, insertions, pairs


def highlow(s, pairs):
    final_s = Counter()
    for k in pairs:
        final_s[k[0]] += pairs[k]
    final_s[s[-1]] += 1
    return max(final_s.values()) - min(final_s.values())


def fx():
    s, insertions, pairs = parsing()

    step=0
    while step<5:

        temp = Counter()
        for k in pairs:
            temp[k[0] + insertions[k]] += pairs[k]
            temp[insertions[k] + k[1]] += pairs[k]
        pairs = temp

        step+=1

    return highlow(s, pairs)

print(fx())


