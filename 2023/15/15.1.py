from functools import reduce

def hash(val, s):
    return ((val + ord(s))*17)%256

def fx(s):
    return sum(reduce(hash, e, 0) for e in open(s).read().strip().split(","))

    # file = open(s).read().strip().split(",")
    # res = 0
    # for e in file:
    #     res += reduce(hash, e, 0)
    #     # curr = 0
    #     # for char in e:
    #     #     curr = hash(curr, char)
    #     #
    #     # res+=curr
    #
    # return res


print(fx('input15.txt'))