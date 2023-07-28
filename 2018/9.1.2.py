from collections import deque, defaultdict

def fx(players, n):

    dudes, circle = defaultdict(int), deque([0,1])
    for number in range(2, n + 1):
        if number%23!=0:
            circle.rotate(2)
            circle.append(number)

        else:
            circle.rotate(-7)
            dudes[number%players] += number + circle.pop()

    return max(dudes.values())


print(fx(9, 25))

print("#########################")
print(fx(10, 1618))
print(fx(13, 7999))
print(fx(17, 1104))
print(fx(21, 6111))
print(fx(30, 5807))


print(fx(493, 71863)) #370601 too high
print(fx(493, 7186300))


"""
    dudes = [0 for _ in range(players)]

    numbers, i, actual_player_idx = [0, 1], 1, 0
    for number in range(2, n+1):
        actual_player_idx+=1
        actual_player_idx%=players

        if number%23 != 0:
            numbers = numbers[:i] + [number] + numbers[i:]
            i+=1
            i= i%len(numbers) + 1

        else:
            dudes[actual_player_idx]+= number + numbers.pop(i-9)
            i-=7

        #print(actual_player_idx+1, numbers, number)
    return max(dudes)


"""