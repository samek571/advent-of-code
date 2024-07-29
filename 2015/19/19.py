import collections


def fx(s, rules):
    dist = set()
    for i in range(len(s)):
        for org, news in rules.items():
            
            if s[i:i+len(org)] == org:
                for new in news:
                    new = s[:i] + new + s[i+len(org):]
                    dist.add(new)
                    
    return len(dist)


s = "input19.txt"
data = [line for line in open(s).read().strip().split("\n")]
dick = collections.defaultdict(list)
for line in data[:-2]:
    tmp = line.split(" => ")
    dick[tmp[0]].append(tmp[-1])


print(dick)
print(fx(data[-1], dick))
