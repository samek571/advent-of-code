# tmp='abcdefghijklmnopqrstuvwxyz'
# h = {}
#
# cnt=0
# for i in tmp:
#     h[cnt]=i
#     cnt+=1
#
# print(h)

hashmap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
rev_hashmap = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
banned = {'i', 'o', 'l'}
def lineup_check(s):
    for idx in range(2,len(s)):
        if hashmap[s[idx]] == hashmap[s[idx-1]]+1 == hashmap[s[idx-2]]+2:
            return True

    return False

def identicale(s):
    hovno = set()
    for idx in range(1,len(s)):
        if s[idx] == s[idx-1]:
            hovno.add(s[idx])

    return len(hovno) >=2

def container(s):
    for l in s:
        if l in banned: return False

    return True


def increaseris(s):

    if s[-1] == 'z':
        idx = len(s)-1
        cnt = 0
        while s[idx] == 'z':
            cnt+=1
            idx-=1

        return s[:idx]+ rev_hashmap[hashmap[s[idx]]+1] + "a"*cnt

    else:
        return s[:-1]+ rev_hashmap[hashmap[s[-1]] + 1]


def fx(s):

    while True:
        s = increaseris(s)

        if lineup_check(s):
            if container(s):
                if identicale(s):
                    return s




print(fx('vzbxxyzz')) #vzbxxyzz

# print(fx('abcdefgh')) #abcdffaa
# print(fx('ghijklmn')) #ghjaabcc
# print(fx('vzbxkghb')) #vzbxxyzz


#vzbxppqr wrong

# print(increaseris('abz'))
# print(increaseris('abzz'))
# print(increaseris('abzzz'))
# print(increaseris('abzzzazz'))
# print(increaseris('abc'))
