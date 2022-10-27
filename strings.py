'''
#question1
Str=input("Enter a string:")
S2=''
for i in range(len(Str)):
    S2+=Str[i]*2
print(S2)

#question2
Str=input("Enter a string:")
for i in range(0,len(Str),2):
    print(Str[i],end='')
print(end='\n')

#question3
Str=input("Enter a string:")
for i in range (len(Str)):
    if ord(Str[i])>=65 and ord(Str[i])<=91:
        a=chr(ord(Str[i])+32)
        print(a,end='')
    elif ord(Str[i])>=91 and ord(Str[i])<=122:
        a=chr(ord(Str[i])-32)
        print(a,end='')
'''
#question4
Str=input("Enter a string:")
Count_upper=0
Count_lower=0
Count_digit=0
Count_symbol=0
Count_words=1
for char in Str:
    if char>='A' and char<='Z':
        Count_upper+=1
    elif char>='a' and char<='z':
        Count_lower+=1
    elif char>='0' and char<='9':
        Count_digit+=1
    elif char==' ':
       Count_words+=1
    else:
        Count_symbol+=1

print('Count upper:',Count_upper)
print('Count lower:',Count_lower)
print('Count digit:',Count_digit)
print('Count symbol:',Count_symbol)
print('Count words:',Count_words)
'''
#question5
Str=input("Enter a string:")
#question6
Str=input("Enter a string:")
'''
