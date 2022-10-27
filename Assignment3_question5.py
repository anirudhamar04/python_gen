s=input("Enter a sentence:")
vowels=['A','a','E','e','I','i','O','o','U','u']
x=-1*len(s)
consonants=0
digits=0
symbols=0
backwards=''
for i in range(-1,x-1,-1):
    backwards+=s[i]
    if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
         if s[i] not in vowels:
            consonants+=1
    elif ord(s[i])>=48 and ord(s[i])<=57:
        digits+=1
    elif ord(s[i])==32:
        continue
    else:
        symbols+=1
    
print("No.of consonants:",consonants)
print("No. of digits:",digits)
print("No. of symbols:",symbols)
print("Reverse of sentence:",backwards)

   
