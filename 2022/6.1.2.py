def inputting():
    moves=open("input6.txt").read().split("\n")
    moves.pop()
    return moves

def fx(n):
    s = inputting()[0]
    print(s)

    cnt=n
    for idx in range(n-1, len(s)):
        stt=set()
        for i in range(n):
            stt.add(s[idx-i])

        if len(stt) == n: return cnt
        cnt+=1

    return cnt

print(fx(14))