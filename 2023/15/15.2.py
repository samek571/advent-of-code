import re
from functools import reduce

def hash(val, s):
    return ((val + ord(s))*17)%256

def fx(s):
    file = open(s).read().strip().split(",")
    boxes = [{} for _ in range(256)]
    for line in file:
        x = re.findall('[a-z]+', line)[0]
        box_id = reduce(hash, x, 0)

        if '=' in line:
            boxes[box_id][x] = int(line.split('=')[-1])
        elif x in boxes[box_id]:
            del boxes[box_id][x]

    return sum(i * sum(val * j for j, val in enumerate(box.values(), start=1)) for i, box in enumerate(boxes, start=1))


print(fx('input15.txt'))