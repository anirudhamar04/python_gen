def CHECK(Str):
    newStr=""
    for i in range(-1,(-1*(len(Str))-1),-1):
        newStr+=Str[i]
    if newStr==Str:
        return True
    else:
        return False
String=input("Enter a string:")
if CHECK(String):
    print("The string ",String,"is a palindrome.")
else:
    print("The string ",String,"is not a palindrome.")