


count=0
cache=dict()
def fx2( round, f_pos, f_score, s_pos, s_score, f_hist=[], s_hist=[], f_throws=[],s_throws=[],cache_round=True ):
    global count
    global cache
    count+=1

    if (f_pos,s_pos,f_score,s_score) in cache :
        return cache[(f_pos,s_pos,f_score,s_score)]
    _win1=0
    _win2=0

    if count % 10000000 ==0:
        print(round,'f:',f_hist,f_throws)
        print(round,'s:',s_hist,s_throws)

    if f_score<21 and s_score<21:

        for thrownum in range(1,4):
            
            if round%6 < 3:
                cache_next_round=False
                scoreaddition=0
                newpos=f_pos
                if round%6 ==2:
                    newpos=(f_pos+thrownum+f_throws[-1]+f_throws[-2])%10
                    if newpos==0: newpos=10
                    scoreaddition=newpos
                if round%6 ==2:
                    cache_next_round=True
                tmp1,tmp2=fx2(round+1, newpos, f_score+scoreaddition, s_pos, s_score, f_hist+[newpos],s_hist,f_throws+[thrownum],s_throws,False)
                _win1+=tmp1
                _win2+=tmp2
            else:
                cache_next_round=False
                scoreaddition=0
                newpos=s_pos
                if round%6 ==5:
                    newpos=(s_pos+thrownum+s_throws[-1]+s_throws[-2])%10
                    if newpos==0: newpos=10
                    scoreaddition=newpos
                if round%6 ==5:
                    cache_next_round=True
                    
                tmp1,tmp2=fx2(round+1, f_pos, f_score, newpos, s_score+scoreaddition, f_hist,s_hist+[newpos],f_throws,s_throws+[thrownum],False)
                _win1+=tmp1
                _win2+=tmp2

        if round%3==2:
            cache[(f_pos,s_pos,f_score,s_score)]=(_win1,_win2)
        return _win1,_win2

    else:
        if f_score>=21:
            _win1=1
            _win2=0
#            print('win ',round,'f:',f_hist)
        else:
            _win1=0
            _win2=1
#            print('win ',round,'s:',s_hist)
        return (_win1,_win2)
                

ways_to_roll=[0 for _ in range(10)]
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            ways_to_roll[i + j + k]+=1;

cache2=dict()
def fx3( f_pos, f_score, s_pos, s_score ):
    global count
    global cache2
    count+=1

    if (f_pos,s_pos,f_score,s_score) in cache2 :
        return cache2[(f_pos,s_pos,f_score,s_score)]

    if f_score >=21:
        return 1,0
    if s_score >=21:
        return 0,1

    total_f_wins =0
    total_s_wins =0

    for sum, cnt  in enumerate(ways_to_roll):
        if sum <3: 
            continue
        
        new_pos = (f_pos + sum) % 10
        if new_pos==0: new_pos = 10
        new_score = f_score + new_pos 

        s_wins, f_wins = fx3(s_pos, s_score, new_pos, new_score)

        total_f_wins += f_wins * cnt
        total_s_wins += s_wins * cnt

    cache2[(f_pos,s_pos, f_score, s_score)]=(total_f_wins, total_s_wins)
    return total_f_wins, total_s_wins

import copy
wins=[0,0]
class PlayerState:
    def __init__(self, _pos=0, _score=0):
        self.pos=_pos
        self.score=_score

    def __str__(self):
        return "["+str(self.pos)+","+str(self.score)+"]"
    
def fr(states, player_on_turn=0 , ways_to_reach_this_state=1):
#    print(states[0],states[1])
    global count
    count+=1
    if count % 100000 ==0:
        print(count/1000)
    for roll in range(3,10):
        new_states = copy.deepcopy(states);
        new_ways = ways_to_reach_this_state * ways_to_roll[roll];

        new_states[player_on_turn].pos += roll;
        if new_states[player_on_turn].pos > 10:
            new_states[player_on_turn].pos -= 10

        new_states[player_on_turn].score += new_states[player_on_turn].pos;

        if new_states[player_on_turn].score >= 21:
            wins[player_on_turn] += new_ways
        else:
            fr(new_states, 1 - player_on_turn, new_ways)

def f2(f,s):
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                ways_to_roll[i + j + k]+=1;

    print( ways_to_roll )
    fr( [ PlayerState(f), PlayerState(s) ] );
    return [wins[0], wins[1]];

                

print("fx2",fx2(0,7,0,5,0))
print("fx3",fx3(7,0,5,0))
#print( f2(4,8) )
#print( f2(7,5) )
#print(count,cache)
