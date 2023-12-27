hsh = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}


def helper(line):
    word = ''
    for letter in line:
        word += letter

        for key, val in hsh.items():
            if key in word or key in word[::-1] or val in word or val in word[::-1]:
                return hsh[key] or hsh[val]

print(sum(int(helper(line) + helper(line[::-1])) for line in open('input1.txt').read().split("\n")[:-1]))



    #'''for some fucking reason regex is incapable of backing by index and 'twone' is considered to be a 21'''
    # for line in inputting(s):
    #     dgts = re.findall('[1-9]|one|two|three|four|five|six|seven|eight|nine', line)
    #     print(line)
    #     print(dgts)
    #     print(int(hsh[dgts[0]]+hsh[dgts[-1]]))
    #     print('')
    #     res += int(hsh[dgts[0]]+hsh[dgts[-1]])
    #return res


