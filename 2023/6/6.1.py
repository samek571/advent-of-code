import re

parse = open('input6.txt').read().split("\n")
times = list(map(int, re.findall('[0-9]+', parse[0])))
distances = list(map(int, re.findall('[0-9]+', parse[1])))

def bs(time, greater_than):
    l, r = 0, time//2
    if r%2==1:
        r-=1

    while l<=r:
        mid = (r+l)//2
        if l==r:
            if mid * (time-mid) == greater_than:
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

res = 1
for case_idx in range(len(times)):
    res *= bs(times[case_idx], distances[case_idx])

print(res)