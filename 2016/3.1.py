moves = open("input3.txt").read().split()

for i in range(len(moves)):
    moves[i]=int(moves[i])

def fx(moves):
    print(moves)
    output=0

    i=2
    while i!=len(moves)+2:
        cigan=[moves[i-2],moves[i-1],moves[i]]

        if cigan[0]+cigan[1]>cigan[2] and cigan[0]+cigan[2]>cigan[1] and cigan[2]+cigan[1]>cigan[0]:
            output+=1

        i+=3

    return output

print(fx(moves))