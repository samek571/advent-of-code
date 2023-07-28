def fx(office, layout):
    maze = [","] * layout
    for i in range(layout):
        maze[i] = [","] * layout

    for x in range(layout):
        for y in range(layout):
            num = x * x + 3 * x + 2 * x * y + y + y * y + office

            num = format(num, 'b')

            ones = 0
            for i in num:
                if i == "1": ones += 1

            if ones % 2 == 0:
                maze[y][x] = "  "
            else:
                maze[y][x] = "[]"


    maze[1][1] = "YY"
    maze[39][31] = "YY"


    for line in maze:
        s = ''
        for char in line:
            s += char
        print(s)

print(fx(1362, 45))
# print(fx(10, 10))
#137 too low
#139 too high
# XD? strasne som sprosty...