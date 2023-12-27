import re

parse = open('input6.txt').read().split("\n")
time = int(''.join(re.findall('[0-9]+', parse[0])))
distance = int(''.join(re.findall('[0-9]+', parse[1])))

def bs(time, greater_than):
    l, r = 0, time//2
    if r%2==1:
        r-=1

    while l<=r:
        mid = (r+l)//2
        if l==r or l==r-1:
            if mid * (time-mid) == greater_than or l==r-1:
                l+=1


            half = time//2
            if time % 2 == 1 and half%2==1:
                return (half-l+1)*2
            else:
                return 1 + time-l*2


        elif mid * (time-mid) < greater_than:
            l = mid + 1

        elif mid * (time-mid) > greater_than:
            r = mid - 1

print(bs(time, distance))
