#i have literally just look at the wiki they hyperlinked and there it was OEIS - A006751
# so i just transalted perl to pytohn...

def look_and_say(start, n):
    current = str(start)
    result = [current]
    for _ in range(n - 1):
        next_sequence = []
        last_char = current[0]
        count = 0

        for char in current:
            if char == last_char:
                count += 1
            else:
                next_sequence.append(f"{count}{last_char}")
                last_char = char
                count = 1
        next_sequence.append(f"{count}{last_char}")  # Append the last counted group
        current = ''.join(next_sequence)
        result.append(current)

    for i in result:
        print(i)

    return len(result[-1])


#part1
#n = int(41)
n = int(51)
start = 3113322113
print(look_and_say(start, n))


#for 3113322113 there is a correct answer for someone else and it is 252594
#issue was that the len(arr) has to be 41 not 40, i.e process is repeated 40times