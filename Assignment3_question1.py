string=input("Enter a string:")
vowels=['A','a','E','e','I','i','O','o','U','u']
x=len(string)
string2=string
for i in range(0,x):
    if string[i] in vowels:
        string2=string2[:i]+'-'+string2[i+1:]
      
print(string)
print(string2)
