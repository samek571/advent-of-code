from collections import defaultdict, Counter

def Parsing():
    moves=open("input6.txt").read().split(",")
    moves[-1]=moves[-1][:1]
    return Counter([int(x) for x in moves])


def fx(moves, n):
    for day in range(n):
        temp=defaultdict(int)
        for key, val in moves.items():
            if key !=0:
                temp[key-1]+=val
            else:
                temp[6]+=val
                temp[8]+=val

        moves=temp
    return sum(moves.values())


print(fx(Parsing(), 80))
print(fx(Parsing(), 256))
print(fx(Parsing(), 256777))
