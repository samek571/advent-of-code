def parsing():
    moves=open("input8.txt").read().split("\n")
    moves.pop()
    return moves

def fx(moves):
    counter=0
    lenght={2,3,4,7}
    for line in moves:
        line = line.replace("|", " ")
        line = line.split()

        for i in line[10:]:
            if len(i) in lenght: counter+=1

    return counter

print(fx(parsing()))
