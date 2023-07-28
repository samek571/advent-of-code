import hashlib

def isNumber(s):
   if(s[0] =='-'):
      s=s[1:]
   #exception handling
   try:
      n = int(s)
      return True
   # catch exception if any error is encountered
   except ValueError:
      return False


def fx():
    output=["_"]*8
    moves = "uqwqemis"
    number=0
    while "_" in output:

        temporar=moves
        temporar+=str(number)
        check= hashlib.md5(temporar.encode())
        check = check.hexdigest()

        s=check[5]
        if check[:5] == "00000" and isNumber(s) == True and int(s)<8:
            print(number)

            if output[int(check[5])] == "_":
                output[int(check[5])] = check[6]

            print(output)
        number+=1

    return output
print(fx())
#69e1906d