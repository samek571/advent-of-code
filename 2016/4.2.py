rooms = open("input4.txt").read().split("\n")
rooms.pop()

def fx(rooms):

    idx=0
    while idx!= len(rooms):
        room=rooms[idx]
        idx+=1
        sector_id=int(room[-10:-7])
        room=room[:-11]
        newroom=''
        shift = sector_id
        allletters="abcdefghijklmnopqrstuvwxyz"

        for i in range(len(room)):
            if room[i]=="-": continue
            bubak=allletters.index(room[i])
            bubak+=shift
            bubak%=26
            newroom+=allletters[bubak]

        room=newroom
        if "northpole" in room:
            print(sector_id)


print(fx(rooms))