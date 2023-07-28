moves=open("input2.txt").read().split("\n")
moves.pop()

def fx(moves):
    depth=horizontalp=0
    for line in moves:
        if "forward" in line: horizontalp+=int(line[-1])
        elif "up" in line: depth+=int(line[-1])
        else: depth-=int(line[-1])

    return depth*horizontalp

print(fx(moves))