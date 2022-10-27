string= input("Enter a string:")
length=-1*len(string)
backwards=''
for i in range(-1,length-1,-1):
    backwards+=string[i]
if backwards==string:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
