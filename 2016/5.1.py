import hashlib

def fx():
    output=''
    moves = ""
    number=0
    while len(output)!=8:

        temporar=moves
        temporar+=str(number)
        check= hashlib.md5(temporar.encode())
        check = check.hexdigest()


        if check[:5] == "00000":
            output+=check[5]
            print(check[5])
        number+=1

    return output
print(fx())