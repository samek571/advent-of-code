import collections


def fx(a,b, num):
    fa = 16807
    fb = 48271
    modd = 2**31-1

    da, db = collections.deque([]), collections.deque([])
    total = 0
    #while total<num:
    for _ in range(num+1):
        a = (fa*a)%modd
        b = (fb*b)%modd

        if a%4 == 0:
            tempa = bin(a)[2:][-16:]
            da.append(tempa)

        if b%8 == 0:
            tempb = bin(b)[2:][-16:]
            db.append(tempb)


        if da and db:
            x,y = da.popleft(), db.popleft()
            if x==y:
                total+=1
                print(total)


    return total


print(fx(65, 8921, 5*10**6))
#print(fx(591, 393, 5*10**6))