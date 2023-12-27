import collections
import re

def gravity_falls(tower, inspected_brick):
    tops_no_bottoms, res = collections.defaultdict(int), 0
    
    for idx, (u,v,w, x,y,z) in enumerate(tower):
        if idx == inspected_brick: continue #testing elimination of 1 brick 

        brick_area = [(a, b) for a in range(u, x+1) for b in range(v, y+1)]
        top = max(tops_no_bottoms[a] for a in brick_area)+1

        for a in brick_area: #position of each pixel
            tops_no_bottoms[a] = top+z-w

        tower[idx] = (u,v,top, x,y,top+z-w) #apply gravity on the brick
        if top < w: #incompetent brick
            res+=1

    #part 1 return 1 (-True) if some bricks fall, we are interested in no chain reaction of falls
    #part 2
    return not res, res

#sorting by z-coord so we go bottom-up brick by brick
#each tower is [x1 y1 z1 x2 y2 z3]
og_tower = sorted([[*map(int, re.findall('[0-9]+',l))] for l in open('input22.txt')], key=lambda b:b[2])

gravity_falls(og_tower, -1)

#testing brick by brick, doing both parts at the same time, see ^^
#i kinda predicted the chain reaction, nothing harder for pt2...
print(*map(sum, zip(*[gravity_falls(og_tower.copy(), idx) for idx in range(len(og_tower))])))