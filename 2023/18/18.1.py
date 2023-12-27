#same shit as in day 10
#https://en.wikipedia.org/wiki/Green's_theorem
def pre(s):
    return [(line.split(' ')[0], int(line.split(' ')[1])) for line in open(s).read().split('\n')[:-1]]

def fx(s):
    x,y = 0,0
    perimeter,area = 0,0
    oracle = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

    for step in pre(s):
        dirr, l = step #dirr because dir is reserved word for directory
        dx, dy = oracle[dirr]

        dx, dy = dx*l, dy*l
        x, y = x+dx, y+dy
        perimeter, area = perimeter+l, area+y*dx


    return area + perimeter//2+1

print(fx('input18.txt'))