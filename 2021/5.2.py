moves=open("input5.txt").read().split("\n")
moves.pop()

def fx(moves):
    overlaps=set()
    encountered=set()

    for row in moves:
        x1, x2, y1, y2, x, y = Parsing(row)


        print(" ")
        if x1==x2: #x==0:
            coords=(y1,y2)
            for i in range(min(coords), max(coords)+1):
                #print(x1, i)

                if (x1, i) in encountered: overlaps.add((x1, i))
                else: encountered.add((x1, i))

        elif y1==y2: #y==0:
            coords=(x1,x2)
            for i in range(min(coords), max(coords)+1):
                #print(i, y1)

                if (i, y1) in encountered: overlaps.add((i,y1))
                else: encountered.add((i, y1))


        else:
            if x1<x2 and y1<y2:
                for i in range(x+1):
                    print(x1+i, y1+i)

                    if (x1+i, y1+i) in encountered: overlaps.add((x1+i,y1+i))
                    else: encountered.add((x1+i, y1+i))

            elif x1<x2 and y1>y2:
                for i in range(x+1):
                    print(x1+i, y1-i)

                    if (x1+i, y1-i) in encountered: overlaps.add((x1+i,y1-i))
                    else: encountered.add((x1+i, y1-i))

            elif x1>x2 and y1<y2:
                for i in range(x + 1):
                    print(x1 - i, y1 + i)

                    if (x1 - i, y1 + i) in encountered: overlaps.add((x1 - i, y1 + i))
                    else: encountered.add((x1 - i, y1 + i))

            else:
                for i in range(x + 1):
                    print(x1 - i, y1 - i)

                    if (x1 - i, y1 - i) in encountered: overlaps.add((x1 - i, y1 - i))
                    else: encountered.add((x1 - i, y1 - i))


    return len(overlaps)


def Parsing(row):
    x1 = x2 = y1 = y2 = 0

    row = row.replace(" -> ", ",").split(",")
    x1 = int(row[0])
    y1 = int(row[1])
    x2 = int(row[2])
    y2 = int(row[-1])
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return (x1,x2,y1,y2,x,y)

print(fx(moves))

# 10630 too low
# 12787 too low