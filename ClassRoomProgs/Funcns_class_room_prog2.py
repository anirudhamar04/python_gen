def Rev_String(string):
    newStr=""
    for i in range(-1,(-(len(string))-1),-1):
        newStr+=string[i]
    return newStr

String=input("Enter a string:")
newString= Rev_String(String)
print(newString)

