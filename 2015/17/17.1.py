#basically 1D knapsack problem, there are mutliple algorithms that have O(2^n) and 
# are effective as early cutting and no redundancy computing but its part1... 

def fx(vols, w, i=0):
    if w == 0:
        return 1

    if w < 0 or i >= len(vols):
        return 0

    include = fx(vols, w - vols[i], i + 1)
    exclude = fx(vols, w, i + 1)

    return include + exclude


s = "input17.txt"
volumes = [int(line) for line in open(s).read().strip().split("\n")]
#volumes = [10,5,5,20,15]
#W = 20
W = 150
print(fx(volumes, W))
