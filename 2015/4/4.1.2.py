import hashlib

def fx():
    output=''
    moves = "iwrupvqb"
    number=0
    while len(output)!=8:

        temporar=moves
        temporar+=str(number)
        check= hashlib.md5(temporar.encode())
        check = check.hexdigest()


        if check[:6] == "000000":
            print(number)
        number+=1

    return output
print(fx())