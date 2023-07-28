#target area: total_x=57..116, total_y=-198..-148

#target area: total_x=20..30, total_y=-10..-5
#total_x [sum to make at least 20, 30]
def fx():
    suitable = 0
    for x in range(11, 116+1):
        for y in range(-198, 200):
            total_x = 0
            total_y = 0
            actual_x = x
            actual_y = y
            while True:
                total_y += actual_y
                actual_y -= 1

                total_x += actual_x
                if actual_x > 0:
                    actual_x -= 1
                elif actual_x < 0:
                    actual_x += 1

                #if 20<=total_x<=30 and -10<=total_y<=-5:
                if 57 <= total_x <= 116 and -198 <= total_y <= -148:
                    suitable+=1
                    break
                elif total_y<-198: break

    return suitable
print(fx())
