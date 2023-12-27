import re
import z3


def pre_p(s):
    hailstones = []

    for line in open(s).read().strip().split("\n"):
        x, y, z, vx, vy, vz = list(map(int, re.findall('-?[0-9]+', line)))  # fucking forgot about negative sign
        slope = vy / vx
        meet = y - slope * x
        hailstones.append((x, y, z, vx, vy, vz, slope, meet))

    return hailstones

#i had to google a bit but i knew there is an equation solver like this, it had to be
#other than that its junior year highschool for me
def fx(s):
    hailstones = pre_p(s)

    x, y, z, vx, vy, vz = z3.Reals("x y z vx vy vz")
    helper = z3.Solver()

    #plane in R_3 is defined by 3 points, if solution exists - other alligns
    #total of 9 equations of 9 different variables
    for t_unproccessed, h in enumerate(hailstones[:3]):
        t = z3.Real(t_unproccessed)
        #helper.add(t > 0) #still interested in future only, but that is retrieved
        helper.add(x + t * vx == h[0] + t * h[3])
        helper.add(y + t * vy == h[1] + t * h[4])
        helper.add(z + t * vz == h[2] + t * h[5])

    helper.check()
    return sum(helper.model()[var].as_long() for var in [x, y, z])



print(fx('input24h.txt'))
print(fx('input24.txt'))
