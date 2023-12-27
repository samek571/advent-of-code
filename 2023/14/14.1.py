def pre_p(s):
    file = open(s).read().strip().split("\n")
    return list(zip(*file))

def fx(s):
    #its ugly as fuck but i wanted to know what the part 2 is so i kept it simple, no additional fixes
    matrix = pre_p(s)
    res = 0
    for line in matrix:
        n = len(line)
        line = list(line) + ["#"] #just for it to count even if last isnt hashtag
        for idx, char in enumerate(line):
            if char == "O":
                res += n
                n -= 1
            elif char == "#":
                n = len(line)-1-1-idx

    return res

#no fixes after submission, no list comprehension nor other shit, just as it is done under 10mins (around +4hours from start tho)
print(fx('input14.txt'))
