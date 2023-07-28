file= open("input1.txt")

def bravcovina (file):
    sum=0
    for r in file:
        r=int(r)
    
        while r > 8:
            r=r//3
            r-=2
            sum+=r
        
    return sum
print(bravcovina (file))
