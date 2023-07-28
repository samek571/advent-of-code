import re


def inputting():
    moves=open("input4.txt").read().split("\n")
    moves.pop()

    nms=[]
    for i in moves:
        x = re.findall('\d+', i)
        tmp=[]
        for y in x:
            tmp.append(int(y))

        nms.append(tmp)

    return nms

def fx():
    moves = inputting()
    print(moves)

    cnt=0
    for line in moves:
        #part1
        # if (line[2] >= line[0] and line[3]<= line[1]) or \
        #     (line[0] >= line[2] and line[1]<= line[3]): cnt+=1

        #part2 some logical mistake idc
        # if line[1]>=line[2] and line[0]>=line[2]:
        #     print(line)
        #     cnt+=1

        stt=set()
        for idx in range(line[0], line[1]+1):
            stt.add(idx)

        for idx in range(line[2], line[3]+1):
            if idx in stt:
                cnt+=1
                break

    return cnt

print(fx())
#960 high
#584 low