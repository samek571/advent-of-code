'''
(cost, +damage, armor) //(0,0,0) for empty

'''

def scenario_fight_gen():
    def handle_item(category, extra_no_usage):
        processed_items = []
        if extra_no_usage:
            processed_items.append((0,0,0))

        category = category.split('\n')
        for line in category[1:]:
            line = line.split()
            processed_items.append((int(line[-3]), int(line[-2]), int(line[-1])))

        return processed_items


    shop_items = [line for line in open("shop.txt").read().strip().split("\n\n")]

    weapons = handle_item(shop_items[0], False)
    armor = handle_item(shop_items[1], True)
    rings_damage = handle_item(shop_items[2], True)[:4]
    rings_defense = [(0,0,0)] + handle_item(shop_items[2], True)[4:]

    possible_scenario = []

    for w in weapons:
        for a in armor:
            for rda in rings_damage:
                for rde in rings_defense:
                    tmp = [0,0,0]

                    for i in range(len(tmp)):
                        tmp[i]+=w[i]+a[i]+rde[i]+rda[i]


                    possible_scenario.append(tmp)
    '''
    pt2 - reverse sort
    '''
    possible_scenario.sort(reverse=True)
    return possible_scenario

#boss/players health damage armor
def fighting(bh,bd,ba,ph,pd,pa):
    while True:
    #while ph > 0 and bh > 0:
        bh -= max(1, pd-ba)
        if bh<=0: return True

        ph -= max(1, bd-pa)
        if ph<=0: return False


#fighting(12,7,2,8,5,5)


def main(phealth):
    bhealth, bdamage, barmor = [int(line.split(": ")[1]) for line in open("input21.txt").read().strip().split("\n")]

    for _possible_senario in scenario_fight_gen():
        cost, pdamage, parmor = _possible_senario
        '''
        pt2 - added NOT
        '''
        if not fighting(bhealth, bdamage, barmor, phealth, pdamage, parmor):
            return cost

print(main(100))

