def parsing():
    moves=open("input7.txt").read().strip().split(",")
    return sorted([int(x) for x in moves])

print(parsing())

def fx(moves):
    print("sumaz:", sum(moves), "len:", len(moves))

    desired = round(sum(moves)/len(moves))-1
    print(desired)

    pole=[]
    fuel=0
    for i in moves:
        fuel+=(abs(i-desired)) * (abs(i-desired)+1)//2
        pole.append((abs(i-desired)) * (abs(i-desired)+1)//2)

    return fuel, pole



print(fx(parsing()))
# 84678839 too low
# 85015849 too high