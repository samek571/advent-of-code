def parsing():
    moves=open("input14.txt").read().split("\n")
    moves.pop()
    s=moves[0]
    insertions = {}

    for i in moves[2:]:
        first = i[0]+i[1]
        second = i[0] + i[-1]
        insertions[first] = second

    return s, insertions

print(parsing())
def highlow(s):
    dick={}

    for i in s:
        if i in dick: dick[i]+=1
        else: dick[i]=1

    return max(dick.values()) - min(dick.values())

def fx():
    s, insertions = parsing()

    step=0
    while step<10:
        news=''
        for i in range(1, len(s)):
            substring=s[i-1]+s[i]
            news += insertions[substring]

        news+=s[-1]
        s = news
        step+=1
        print(s)

    return highlow(s)

print(fx())


