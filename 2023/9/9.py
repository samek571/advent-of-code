def dfs(arr):
    if all(e == 0 for e in arr) or not arr: return 0

    new_arr = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    return arr[-1] + dfs(new_arr)


def pre_process(s, part):
    res = 0
    for line in open(s).read().split("\n")[:-1]:
        if part == 1:
            res += dfs(list(map(int, line.split())))
        else:
            res += dfs(list(map(int, line.split()))[::-1])

    return res

print(pre_process('input9.txt', 1))
print(pre_process('input9.txt', 2))
