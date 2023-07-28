file= open("input1.txt","r")

def bravcovina ():
    sum=0
    for r in file:
        r=int(r)
        r=r//3
        r-=2
        sum+=r
    return sum
print(bravcovina ())
