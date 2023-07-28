

def fx():

    firstplayer_pos=7
    firstplayer_score=0
    secondplayer_pos=5
    secondplayer_score=0

    round=0
    while secondplayer_score<1000 and firstplayer_score<1000:

        one_move=0
        for i in range(3):
            one_move+=dice
            dice+=1
            dice%=100
            number_of_time_rolled+=1

        #first player
        if round%2==0:
            firstplayer_pos += one_move
            firstplayer_pos %= 10

            if firstplayer_pos == 0: firstplayer_pos = 10
            firstplayer_score+=firstplayer_pos
            round += 1

        #second player
        else:
            secondplayer_pos += one_move
            secondplayer_pos %= 10

            if secondplayer_pos == 0: secondplayer_pos = 10
            secondplayer_score+=secondplayer_pos
            round += 1


    return max(firstplayer_score, secondplayer_score)



win1=0
win2=0
count=0
def fx2( round, f_pos, f_score, s_pos, s_score, f_hist=[], s_hist=[], f_throws=[],s_throws=[] ):
    global win1
    global win2
    global count
    count+=1

    if count % 10000000 ==0:
        print(count)
        print(round,'f:',f_hist, f_throws)
        print(round,'s:',s_hist,s_throws)

    if f_score<21 and s_score<21:

        for thrownum in range(1,4):
            
            if round%6 < 3:
                scoreaddition=0
                newpos=f_pos
                if round%6 ==2:
                    newpos=(f_pos+thrownum+f_throws[-1]+f_throws[-2])%10
                    if newpos==0: newpos=10
                    scoreaddition=newpos
                fx2(round+1, newpos, f_score+scoreaddition, s_pos, s_score, f_hist+[newpos],s_hist,f_throws+[thrownum],s_throws)
            else:
                scoreaddition=0
                newpos=s_pos
                if round%6 ==5:
                    newpos=(s_pos+thrownum+s_throws[-1]+s_throws[-2])%10
                    if newpos==0: newpos=10
                    scoreaddition=newpos
                    
                fx2(round+1, f_pos, f_score, newpos, s_score+scoreaddition, f_hist,s_hist+[newpos],f_throws,s_throws+[thrownum])
    else:
        if f_score>=21:
            win1+=1
#            print('win ',round,'f:',f_hist)
        else:
            win2+=1
#            print('win ',round,'s:',s_hist)
                

fx2(0,7,0,5,0)
print(win1,win2,count)
