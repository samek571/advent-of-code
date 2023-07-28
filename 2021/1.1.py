moves=open("input1.txt").read().split("\n")
moves.pop()
def fx(moves):
    hovno =[]
    for i in moves:
        hovno.append(int(i))

    output=0
    i=1
    while i!=len(hovno):
        if hovno[i-1]<hovno[i]: output+=1
        i+=1

    return output
print(fx(moves))