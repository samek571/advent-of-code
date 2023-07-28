import re
 
def load_data( path):
    data = []
    f=open(path, 'r')
    for line in f:
        splitted = re.match(r'(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$', line).groups()
        data.append([splitted[0]] + [int(i) for i in splitted[1:]])
    return data
 
 
def overlapping_cuboid(cuboid_a, cuboid_b):
    max_x, max_y, max_z = (max(cuboid_a[0], cuboid_b[0]),  max(cuboid_a[2], cuboid_b[2]),  max(cuboid_a[4], cuboid_b[4]))
    min_xp, min_yp, min_zp = (min(cuboid_a[1], cuboid_b[1]),  min(cuboid_a[3], cuboid_b[3]),  min(cuboid_a[5], cuboid_b[5]))
    if min_xp - max_x >= 0 and min_yp - max_y >= 0 and min_zp - max_z >= 0:
        return max_x, min_xp, max_y,  min_yp, max_z, min_zp
 
 
def count_on_cuboids(data):
    on_count = 0
    counted_zones = []
    for d in reversed(data):
        mode, cuboid = d[0], d[1:]
        x1, x2, y1, y2, z1, z2 = cuboid
        if mode == 'on':
            dead_cuboids = []
            for overlap_cuboid in [overlapping_cuboid(zone, cuboid) for zone in counted_zones]:
                if overlap_cuboid:
                    dead_cuboids.append(('on', overlap_cuboid[0],overlap_cuboid[1],overlap_cuboid[2],overlap_cuboid[3],overlap_cuboid[4],overlap_cuboid[5]))
            on_count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            on_count -= count_on_cuboids(dead_cuboids)
        counted_zones.append(cuboid)
    return on_count
 

############# method 2 ######
def count_cuboid(x1,x2,y1,y2,z1,z2):
        if x2<x1 or y2<y1 or z2<z1:
            return 0
        return (x2 - x1) * (y2 - y1) * (z2 - z1)

def a_minus_b(a, b):
    x1,x2,y1,y2,z1,z2=0,1,2,3,4,5
    if not (a[x1] < b[x2] and a[x2] > b[x1]
        and a[y1] < b[y2] and a[y2] > b[y1]
        and a[z1] < b[z2] and a[z2] > b[z1]):
        return [a]
    else:
        b = [  min(max(b[x1], a[x1]), a[x2]), min(max(b[x2], a[x1]), a[x2]),
               min(max(b[y1], a[y1]), a[y2]), min(max(b[y2], a[y1]), a[y2]),
               min(max(b[z1], a[z1]), a[z2]), min(max(b[z2], a[z1]), a[z2]) ]

        result=[]
        if    count_cuboid(a[x1],   b[x1]-0, a[y1],   a[y2],   a[z1],   a[z2])>0: result.append([a[x1],   b[x1]-0, a[y1],   a[y2],   a[z1],   a[z2]])
        if    count_cuboid(b[x2]+0, a[x2],   a[y1],   a[y2],   a[z1],   a[z2])>0: result.append([b[x2]+0, a[x2],   a[y1],   a[y2],   a[z1],   a[z2]])
        if    count_cuboid(b[x1],   b[x2],   a[y1],   b[y1]-0, a[z1],   a[z2])>0: result.append([b[x1],   b[x2],   a[y1],   b[y1]-0, a[z1],   a[z2]])
        if    count_cuboid(b[x1],   b[x2],   b[y2]+0, a[y2],   a[z1],   a[z2])>0: result.append([b[x1],   b[x2],   b[y2]+0, a[y2],   a[z1],   a[z2]])
        if    count_cuboid(b[x1],   b[x2],   b[y1],   b[y2],   a[z1],   b[z1]-0)>0: result.append([b[x1],   b[x2],   b[y1],   b[y2],   a[z1],   b[z1]-0])
        if    count_cuboid(b[x1],   b[x2],   b[y1],   b[y2],   b[z2]+0, a[z2])>0: result.append([b[x1],   b[x2],   b[y1],   b[y2],   b[z2]+0, a[z2]])
    return result
      
def method2(data):
    C = []
    for row in data:
        cmd, x1, x2, y1, y2, z1, z2 = row 
    
        cuboid = [x1, x2+1, y1, y2+1, z1, z2+1]
        tmp=[]
        for c2 in C:
            for c3 in a_minus_b(c2,cuboid):
                tmp.append(c3)
        C=tmp
        if cmd == 'on':
            C.append(cuboid)

    return sum( [count_cuboid(*c) for c in C] )

##########
data = []
for row in load_data('22.txt'):
    x1, x2, y1, y2, z1, z2 = row[1:]
    if x1 <= 50 and x2 >= -50 and y1 <= 50 and y2 >= -50 and z1 <= 50 and z2 >= -50:
        data.append(row)

on_count = count_on_cuboids(data)
print( on_count)

print("metoda2:", method2(data))
 
 
data = load_data('22.txt')
on_count = count_on_cuboids(data)
print(on_count)
print("metoda2",method2(data))



