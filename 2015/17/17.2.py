#basically 1D knapsack problem, there are mutliple algorithms that have O(2^n) and
# are effective as early cutting and no redundancy computing but its part1...

def _helper(vols, w, i=0, cnt=0):
    if w == 0:
        return cnt

    if w < 0 or i >= len(vols):
        return float('inf')

    include = _helper(vols, w - vols[i], i + 1, cnt + 1)
    exclude = _helper(vols, w, i + 1, cnt)

    return min(include, exclude)


def fx(vols, w, i=0, cnt=0, min_containers=float('inf')):
    if w == 0:
        return 1 if cnt == min_containers else 0

    if w < 0 or i >= len(vols):
        return 0

    include = fx(vols, w - vols[i], i + 1, cnt+1, min_containers)
    exclude = fx(vols, w, i + 1, cnt, min_containers)

    return include + exclude


s = "input17.txt"
volumes = [int(line) for line in open(s).read().strip().split("\n")]
#volumes = [10,5,5,20,15]
W = 150
#W = 20

min_containers = _helper(volumes, W)
print(fx(volumes, W, min_containers=min_containers)) #why the fuck do i have to do x=x ??
#181 too high