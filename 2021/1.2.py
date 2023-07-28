moves=open("input1.txt").read().split("\n")
moves.pop()
def fx(moves):
    hovno =[]
    for i in moves:
        hovno.append(int(i))

    output=0

    # if hovno[0]<hovno[1]: output+=1
    # elif hovno[0]+hovno[1]<hovno[0]+hovno[1]+hovno[2]: output+=1

    i=2
    while i!=len(hovno):
        if hovno[i-3]<hovno[i]: output+=1
        i+=1

    return output
print(fx(moves))
#1191 too high
#1150 too low