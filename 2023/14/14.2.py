from itertools import islice

def shift(matrix, north_west):
    #pretty smart trick;
    #splitting by #, then every O gets shifted left (.ljust (left justify)) and rest si filled with '.'
    #these sections are generated #times so just join them

    #could be a oneliner but i am no psychopath
    if north_west: #do .ljust for north and west
        return ["#".join(("O" * section.count("O")).ljust(len(section), ".") for section in "".join(row).split("#")) for row in matrix]
    
    else: # .rjust so there is south and east covered
        return ["#".join(("O" * section.count("O")).rjust(len(section), ".") for section in "".join(row).split("#")) for row in matrix]


def one_cycle(matrix):
    #north + west + south + east from the innermost
    #again could be a oneliner but i chose not to do it
    matrix = shift(list(zip(*matrix)), True)
    matrix = shift(list(zip(*matrix)), True)
    matrix = shift(list(zip(*matrix)), False)
    matrix = shift(list(zip(*matrix)), False)

    return matrix


def fx(s):
    matrix = list(open(s).read().strip().split("\n"))
    cache = {} #dictionary to store the previous cases

    for i in range(10**9):
        matrix_tupled = tuple(matrix)
        if matrix_tupled in cache: #if once we have been there, its pre-defined already, nothing new will happen
            prev_i = cache[matrix_tupled]
            target_i = prev_i + ((10**9 - prev_i) % (i - prev_i))

            #next is a trick that allows us to travel even in unordered dict
            #by slice we get the element
            matrix = next(islice(cache.keys(), target_i, target_i + 1))
            break

        cache[matrix_tupled] = i
        matrix = one_cycle(matrix)

    #kinda trick to iterate from back, didnt think of that in part 1, and i refuse to edit, it really is without edits after submission...
    return sum(row_load * row.count("O") for row_load, row in zip(range(len(matrix), 0, -1), matrix))


print(fx('input14.txt'))