string=input("Enter a sentence:")
s2=string
alpha=0
for x in range(0,len(string)):
    
    if string[x].isspace():
        s2=s2[:x]+'\n'+s2[x+1:]
        
    elif string[x]=='-':
        s2=s2[:x]
        break
for i in range(0,len(string)):
    if string[i].isalpha():
        alpha+=1
    elif string[i].isdigit():
        string=string[:i]+'*'+string[i+1:]

print(s2)
print(string)
print("No. of alphabets =",alpha)
