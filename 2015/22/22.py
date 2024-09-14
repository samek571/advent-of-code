from copy import deepcopy


#(manacost, dmg, hp, armor, mana, lifespan, index)
missile = (53, 4, 0, 0, 0, 0, 0)
drain = (73, 2, 2, 0, 0, 0, 1)
shield = (113, 0, 0, 7, 0, 6, 2)
poison = (173, 3, 0, 0, 0, 6, 3)
recharge = (229, 0, 0, 0, 101, 5, 4)
spells = [missile, drain, shield, poison, recharge]
res = float("inf")


#b/p stands for boss player
'''
dfs algo, unlike in day 21 we could have used greedy due to deterministic algorithm
TOGGLE line below for pt2
'''
partTwo = True
def fx(bhp, php, pmana, active_spells, p_turn, mana_used):
    bdmg = 10
    parmor = 0

    if partTwo and p_turn:
        php -= 1
        if php <= 0:
            return False

    new_active_spells = []
    for active_spell in active_spells:
        if active_spell[5] >= 0:
            bhp -= active_spell[1]
            php += active_spell[2]
            parmor += active_spell[3]
            pmana += active_spell[4]

        new_active_spell = (
        active_spell[0], active_spell[1], active_spell[2], active_spell[3], active_spell[4], active_spell[5] - 1,
        active_spell[6])
        if new_active_spell[5] > 0:
            new_active_spells.append(new_active_spell)

    if bhp <= 0:
        global res
        if mana_used < res:
            res = mana_used
        return True

    if mana_used >= res:
        return False

    if p_turn:
        for i in range(len(spells)):
            spell = spells[i]
            spell_already_activated = False
            for j in range(len(new_active_spells)):
                if new_active_spells[j][6] == spell[6]:
                    spell_already_activated = True
                    break

            spell_mana_cost = spell[0]
            if spell_mana_cost <= pmana and not spell_already_activated:
                tmp = deepcopy(new_active_spells)
                tmp.append(spell)
                fx(bhp, php, pmana - spell_mana_cost, tmp, False, mana_used + spell_mana_cost)
    else:
        php += parmor - bdmg if parmor - bdmg < 0 else -1
        if php > 0:
            fx(bhp, php, pmana, new_active_spells, True, mana_used)


fx(71, 50, 500, [], True, 0)
print(res)