
'''part1'''
print(sum(line.count("(") for line in open('input1.txt').read().split("\n")) - sum(line.count(")") for line in open('input1.txt').read().split("\n")))

'''part2'''
floor = 0
print(next(i for i, c in enumerate(open('input1.txt').read().strip(), 1) if (floor := floor + (1 if c == '(' else -1)) < 0))
