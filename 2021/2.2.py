moves=open("input2.txt").read().split("\n")
moves.pop()

def fx(moves):
    depth=horizontalp=aim=0
    for line in moves:
        if "forward" in line:
            horizontalp+=int(line[-1])
            depth+= aim * int(line[-1])
        elif "up" in line: aim+=int(line[-1])
        else: aim-=int(line[-1])

    return depth*horizontalp

print(fx(moves))