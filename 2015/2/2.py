file =[line for line in open("input2.txt").read().strip().split("\n")]

res1 = sum((2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
             for l, w, h in (map(int, line.split('x')) for line in file)))

res2 = sum((2*min(l+w, w+h, h+l) + l*w*h
            for l, w, h in (map(int, line.split('x')) for line in file)))

print(res1)
print(res2)