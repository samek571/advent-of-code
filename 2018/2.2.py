from collections import defaultdict

def inputting():
    return [s for s in open("input2.txt").read().split("\n")][:-1]


def fx():
    moves = inputting()
    total=0

    for w1 in moves:
        for w2 in moves:

            diff = 0
            the_idx=0
            for char in range(min(len(w2), len(w1))):
                if w1[char] != w2[char]:
                    diff+=1
                    the_idx = char
                if diff>1: break

            if diff == 1: print (w2[the_idx], w1)

    return total

print(inputting())
print(fx())
lufjygedpvfbhftxiwnaorzmq
