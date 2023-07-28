def parsing():
    moves=open("input13.txt").read().split("\n")
    moves.pop()

    foldings=[]
    dots=[]
    for i in moves:
        if "fold" in i:
            number=''
            for char in i:
                if char.isnumeric(): number+=char

            if "x" in i: foldings.append(("x", int(number)))
            else: foldings.append(("y", int(number)))

        elif i == "": continue
        else:
            i=i.split(",")
            dots.append([int(i[-1]), int(i[0])])

    maxx,maxy= 0, 0
    for i in dots:
        maxx = max(maxx, i[0])
        maxy = max(maxy, i[1])

    paper = []
    for i in range(maxx+1):
        paper.append(["."]*(maxy+1))

    for i in dots:
        paper[i[0]][i[1]]="#"

    # for i in paper:
    #     print(i)
    # print("")
    return paper, foldings



def foldy(paper, fold):
    lenght = len(paper)
    fold+=1

    for lineidx in range(fold):
        for char in range(len(paper[0])):
            if paper[lenght-lineidx-1][char]=="#" or paper[lineidx][char] == "#":
                paper[lineidx][char] = "#"


    for i in paper[:fold-1]:
        print(i)

    print("")
    return paper[:fold-1]



def foldx(paper, fold):
    lineidx=0
    for line in paper:
        second = line[fold+1:][::-1]
        first = line[:fold]
        #print(first, second)

        for char in range(len(first)):
            if first[char] == "#" or second[char] == "#":
                paper[lineidx][char] = "#"

        paper[lineidx] = paper[lineidx][:fold]

        lineidx+=1

    return paper



def fx():
    paper, foldings = parsing()
    output=0

    for i in foldings:
        if i[0]=="y":
            paper = foldy(paper, i[1])
        else:
            paper = foldx(paper, i[1])

        for i in paper:
            print(i)

        for line in range(len(paper)):
            for char in range(len(paper[0])):
                if paper[line][char] == "#": output+=1

        return output


print(fx())



