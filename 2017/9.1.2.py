import re

# def fx():
#     file = open("input9.txt").read().split("\n")
#
#
#     def scoreGroups(stream, score, depth):
#         if stream and stream[0] == "}": scoreGroups(stream[1:], score, depth-1)
#         else: scoreGroups(stream[1:], score + depth, depth + 1)
#
#
#     for i in range(2):
#         f=file[i]
#
#         ignor = re.findall("!.", f)
#         garbage = re.findall("<.*?>", f)
#         notgroup = re.findall("[^{}]", f)
#
#         cleaner = f.replace(ignor, "")
#
#         return scoreGroups([cleaner.replace(garbage, "").replace(notgroup, "")])
#
# print(fx())


def fx():
    file = open("input9.txt")
    f = file.readline()

    totalsum, garbage, nested_level = 0, 0, 0

    char_idx=0
    while char_idx < len(f):
        if f[char_idx] == "<":
            char_idx+=1

            while f[char_idx] != ">":
                if f[char_idx] == "!": char_idx+=1
                else: garbage+=1


                char_idx+=1

        elif f[char_idx] == "{": nested_level+=1
        elif f[char_idx] == "}":
            totalsum += nested_level
            nested_level-=1

        char_idx+=1

    return totalsum, garbage
print(fx())

#too high 290830
#too low 2969