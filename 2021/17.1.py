# x [11, 14]
# y [ ]
#target area: x=57..116, y=-198..-148

def fx():
    ymaxes=set()
    for x in range(11, 14+1):
        for y in range(3,100000):
            before = y*(y+1)//2

            gravitation=0
            while gravitation<148:
                y+=1
                gravitation+=y

            if gravitation<=198: ymaxes.add(before)

    return max(ymaxes)
print(fx())

#137 too low