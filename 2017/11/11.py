moves = open("input11.txt","r").readline().strip().split(",")

def fx(moves):
    x=0
    y=0
    for i in moves:
        if i == "ne":
            y += 1
        if i == "se":
            x += 1
        if i == "n":
            y += 1
            x -= 1
        if i == "s":
            x += 1
            y -= 1
        if i == "nw":
            x -= 1
        if i == "sw":
            y -= 1
    return x

print(fx(moves))