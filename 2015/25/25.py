import re

def find_position(row, column):
    return ((row + column - 1) * ((row + column - 1) - 1)) // 2 + column


#it is possoble to not have 2 more lines but the computtational time would be way too high
target_position = find_position(*[int(num) for num in re.findall(r'\d+', "".join([line for line in open('input25.txt').read().strip().split("\n")]))])
code, idx = 20151125, 1
while idx < target_position:
    code, idx = (code * 252533) % 33554393, idx+1

print(code)
