import re


def inputting():
    moves=open("input5.txt").read().split("\n")
    moves.pop()

    q=[]
    for i in moves:
        tmp=[]
        if "move" in i:
            x = re.findall("\d+", i)
            for num in x:
                tmp.append(int(num))

            q.append(tmp)

    return q





def fx():
    q = inputting()
    towers = [
        ["hovnocuc"],
        ["G", "D", "V", "Z", "J", "S", "B"],
        ["Z", "S", "M", "G", "V", "P"],
        ["C", "l", "B", "S", "W", "T", "Q", "F"],
        ["H", "J", "G", "W", "M", "R", "V", "Q"],
        ["C", "L", "S", "N", "F", "M", "D"],
        ["R", "G", "C", "D"],
        ["H", "G", "T", "R", "J", "D", "S", "Q"],
        ["P", "F", "V"],
        ["D", "R", "S", "T", "J"]
    ]

    # towers = [
    #     ["som dogrcany"],
    #     ["Z", "N"],
    #     ["M", "C", "D"],
    #     ["P"]
    # ]

    #part1
    # for cmnd in q:
    #     for i in range(cmnd[0]):
    #         pooped = towers[cmnd[1]].pop()
    #         towers[cmnd[2]].append(pooped)

    #part2
    for cmnd in q:
        tmp = []
        for i in range(cmnd[0]):
            pooped = towers[cmnd[1]].pop()
            tmp.append(pooped)

        tmp = tmp[::-1]
        towers[cmnd[2]] = towers[cmnd[2]] + tmp

    s=''
    for i in towers[1:]:
        s+=i[-1]

    return s

print(fx())
