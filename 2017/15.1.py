
def fx(a,b, num):
    fa = 16807
    fb = 48271
    modd = 2**31-1

    seen = set()
    total = 0 ; cnt = 0
    for i in range(num+1):
        cnt+=1
        a = (fa*a)%modd
        b = (fb*b)%modd

        tempa = bin(a)[2:][-16:]
        tempb = bin(b)[2:][-16:]
        if tempb == tempa: total+=1


        if cnt%10000: print(cnt//100000)

    return total



#print(fx(65, 8921, 40*10**6))
#print(fx(591, 393, 40*10**6))
print(fx(591, 393, 5*10**6))