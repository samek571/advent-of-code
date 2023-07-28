def parsing():
    moves=open("input7.txt").read().strip().split(",")
    return sorted([int(x) for x in moves])

print(parsing())

def fx(moves):

    desired = (moves[len(moves)//2] + moves[len(moves)//2+1]) //2
    print(desired)

    fuel=0
    for i in moves:
        #fuel+=abs(i-desired)
        fuel+=abs(i-desired)

    return fuel



print(fx(parsing()))