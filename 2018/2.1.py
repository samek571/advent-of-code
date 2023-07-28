from collections import defaultdict

def inputting():
    return [s for s in open("input2.txt").read().split("\n")]


def fx():
    moves = inputting()
    s, t = 0, 0

    for line in moves:
        dick = defaultdict(int)
        for char in line:
            dick[char] += 1

        for val in dick.values():
            if val == 2:
                s+=1
                break

        for val in dick.values():
            if val == 3:
                t += 1
                break

    return s*t

print(inputting())
print(fx())

#too high 12559
#too hight 11880