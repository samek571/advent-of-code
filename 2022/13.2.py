import re
import collections

def inputting(s):
    matrix=open(s).read().split("\n")
    matrix.pop()
    return matrix

def compare(left, right):
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            res = compare(l, r)
        else:
            res = r - l
        if res != 0:
            return res
    return len(right) - len(left)

def fx(s):
    matrix = inputting(s)

    # Convert each row of the matrix to a list of values
    rows = [list(map(eval, row.split())) for row in matrix if row.strip()] + [[[2]], [[6]]] + [[]] #manually counted fucking empty bars - there is just one


    # Sort the list of rows using selection sort
    for i in range(len(rows)):
        min_index = i
        for j in range(i+1, len(rows)):
            if compare(rows[j], rows[min_index]) < 0:
                min_index = j
        rows[i], rows[min_index] = rows[min_index], rows[i]

    rows = rows[::-1]
    #for i in rows: print(i)

    return rows.index([[2]]) * rows.index([[6]])


print(fx(s='input13.txt'))
print(fx(s='input13h.txt'))
