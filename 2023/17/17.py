import heapq

#d for distance and dirr for dirrection
def fx_DlKSXTRAAAA_(s, min_d, max_d):
    matrix = [[int(y) for y in x] for x in open(s).read().strip().split('\n')]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] #it needs to be in this specific order because
    # end might come sooner from behind (the non-beneficiary branch, {pun}), our primary objection is to
    # move down and right, dijkstra will take care of the rest

    # cost, x, y, disallowedDirection
    q = [(0, 0, 0, -1)]
    heapq.heapify(q)
    seen = set()
    cache = {}
    
    while q:
        cost, x, y, rev_erse = heapq.heappop(q)
        if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
            return cost
        
        if (x, y, rev_erse) in seen: continue
        seen.add((x, y, rev_erse))

        #we are holding heading (rotation) and as well the new step in iterable
        for dirr in range(4):
            curr_cost = 0
            # we are allowed to rotate only 90deg
            if dirr == rev_erse or (dirr + 2) % 4 == rev_erse: continue
            
            #has to be 1 and not min_d because we are dependent on the traveled route from 1 to min_d
            #see the REF line vv
            for d in range(1, max_d + 1): #d as distance, how long we walk in the dirr direction
                i, j = x + dirs[dirr][0] * d, y + dirs[dirr][1] * d
                if 0<=i<len(matrix) and 0<=j<len(matrix[0]): #within board
                    
                    #REF see the comment ^^
                    curr_cost += matrix[i][j]
                    if d < min_d: continue

                    new_cost = cost + curr_cost
                    if (i, j, dirr) in cache and cache[(i, j, dirr)] > new_cost:
                        cache[(i, j, dirr)] = new_cost

                    heapq.heappush(q, (new_cost, i, j, dirr))


print(fx_DlKSXTRAAAA_('input17.txt',1, 3))
print(fx_DlKSXTRAAAA_('input17.txt',4, 10))
#pt2 had to be either increased minimal_or_maximal or max heat that can be done
#since we are doing 17th day it was kinda predictable and minimal was shock a bit, but luckily it was easily implementable