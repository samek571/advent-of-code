import collections
import re


def pre_p(s):
    tmp = [line for line in open(s).read().strip().split("\n")]

    bot_stash = collections.defaultdict(set)
    bot_decision = collections.defaultdict(tuple)
    for line in tmp:
        nums = [int(i) for i in re.findall('\d+', line)]
        if len(nums)==3:
            action_parts = line.split()
            low_to_type = 'bot' if 'bot' in action_parts[5] else 'output'
            high_to_type = 'bot' if 'bot' in action_parts[10] else 'output'
            bot_decision[nums[0]] = ((low_to_type, nums[1]), (high_to_type, nums[-1]))

            #bot_decision[nums[0]] = (("bot", nums[1]), ("bot", nums[2]))
        else:
            bot_stash[nums[1]].add(nums[0])

    return bot_stash, bot_decision

def pt1(s):
    bot_stash, bot_decision = pre_p(s)


    outputs = collections.defaultdict(int)
    running = True

    while running:
        running = False
        for bot in list(bot_stash):
            if len(bot_stash[bot]) == 2:
                low, high = sorted(bot_stash[bot])
                if low == 17 and high == 61:
                    return bot, outputs

                l, h = bot_decision[bot]
                bot_stash[bot].clear()
                if l[0] == 'bot':
                    bot_stash[l[1]].add(low)
                else:
                    outputs[l[1]] = low

                if h[0] == 'bot':
                    bot_stash[h[1]].add(high)
                else:
                    outputs[h[1]] = high
                running = True

    return outputs


print(pt1('input10.txt'))
