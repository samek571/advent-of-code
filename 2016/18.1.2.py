first=open("input18.txt").read().strip()

def fx(first):
    output=[first]


    while len(output)!=400000:
        newline=''

        if output[-1][1] == "^": newline+="^"
        else: newline+="."

        i=1
        while i!=len(output[0])-1:
            if output[-1][i-1] == output[-1][i+1]: newline+="."
            else: newline+="^"
            i+=1

        if output[-1][-2] == "^": newline+="^"
        else: newline += "."

        output.append(newline)


    total=0
    for i in output:
        for ch in i:
            if ch == ".":
                total+=1
        print(i)

    print(total)


print(fx(first))


