from functools import lru_cache
import re

# def dfs(s, L, idx, flag):
#     #flag for not necesarrily placing "." if the s ends with #####
#
#     # exit
#     if idx == len(s):
#         return 1 if not L else 0  # either it is a valid or invalid formation
#
#     #just skip
#     if s[idx] == '.':
#         return dfs(s, L, idx + 1, flag)
#
#     elif s[idx] == '#':
#         if L:
#             # Check if the sequence of '#' can be placed
#             end_index = idx + L[0]
#             end_index = min(end_index, len(s))
#
#             # Check for valid '#' sequence
#             if all(c in ['#', '?'] for c in s[idx:end_index]) and (end_index == len(s) or s[end_index] in ['.', '?']):
#                 # If end_index is at the end of s and flag is True, or if the next character is valid
#                 if end_index == len(s) and flag:
#                     return dfs(s, L[1:], end_index, flag)
#                 elif end_index < len(s):
#                     return dfs(s, L[1:], end_index + 1, flag)
#
#     elif s[idx] == '?':
#         count = 0
#         #'?' gets mapped to "#"
#         if L:
#             end_index = idx + L[0]
#             end_index = min(end_index, len(s))
#
#             # if it is possible to place "#" L[0] times
#             if all(c in ['#', '?'] for c in s[idx:end_index]) and (end_index == len(s) or s[end_index] in ['.', '?']):
#                 if end_index == len(s) and flag:
#                     count += dfs(s, L[1:], end_index, flag)
#                 elif end_index < len(s):
#                     count += dfs(s, L[1:], end_index + 1, flag)
#
#         #'?' gets mapped to "."
#         count += dfs(s, L, idx + 1, flag)
#
#         return count
#
#     #if it isnt valid formation
#     return 0


@lru_cache() #little trick
def dfs(s, L, idx):
    #1 if possible formationm otherwise 0
    if not L:
        return int(all(s != '#' for s in s[idx:]))

    #wont be possible to finish
    if len(s) - idx < sum(L):
        return 0

    #skip because it has nothing to add, just move idx and follow recursion pattern
    if s[idx] == '.':
        return dfs(s, L, idx + 1)

    #case in which "?" gets mapped to "#"
    count = 0
    if s[idx] in ['#', '?']:
        #if it is possible to place "#" L[0] times
        if all(s != '.' for s in s[idx:idx + L[0]]) and (len(s) > idx + L[0] and s[idx + L[0]] != '#' or len(s) <= idx + L[0]):
            count = dfs(s, tuple(L[1:]), idx + L[0] + 1)

    #'?' gets mapped to "."
    moved = 0
    if s[idx] == '?':
        moved = dfs(s, L, idx + 1)

    return count + moved


def pre_p(s):
    #could be a one liner
    #return sum(dfs(line.split()[0], tuple(map(int, re.findall('[0-9]+', line))), 0) for line in open(s).read().split("\n")[:-1]), sum(dfs(((line.split()[0] + '?') * 5)[:-1], tuple(map(int, re.findall('[0-9]+', line))) * 5, 0) for line in open(s).read().split("\n")[:-1])

    res1, res2 = 0, 0
    for line in open(s).read().split("\n")[:-1]:
        L = tuple(map(int, re.findall('[0-9]+', line)))
        txt = line.split()[0]
        res1+=dfs(txt, L, 0)

        txt = ((txt+'?')*5)[:-1]
        L = L*5
        res2+=dfs(txt, L, 0)
    return res1, res2
        
print(pre_p('input12.txt'))