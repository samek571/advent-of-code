moves = open("input3.txt").read().split()

for i in range(len(moves)):
    moves[i]=int(moves[i])

def fx(moves):
    print(moves)
    output=0

    k=0
    while k!=len(moves):
        charged=3
        i=k
        while charged!=0:
            cigan=[moves[i],moves[i+3],moves[i+6]]

            if cigan[0]+cigan[1]>cigan[2] and cigan[0]+cigan[2]>cigan[1] and cigan[2]+cigan[1]>cigan[0]:
                output+=1

            charged-=1
            i+=1

        k+=9

    return output

print(fx(moves))