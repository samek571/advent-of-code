'''pt1'''
import re
def filterino(s):
    return sum([int(match) for match in re.findall("\d+|-\d+", s)])

print(filterino(open("input12.txt").read()))


'''pt2'''
# isinstance is a handy tool
import json

def helper(junk):
    if isinstance(junk, dict):
        if "red" in junk.values():
            return {}
        return {k: helper(v) for k, v in junk.items()}
    elif isinstance(junk, list):
        return [helper(item) for item in junk]
    
    return junk

def parser(s):
    with open(s, 'r') as file:
        return json.load(file, object_hook=helper)


def main(junk):
    if isinstance(junk, dict):
        return sum(main(v) for v in junk.values())
    elif isinstance(junk, list):
        return sum(main(item) for item in junk)
    elif isinstance(junk, int):
        return junk
    return 0

print(main(parser("input12.txt")))
