string=input("Enter a sentence:")
LCASE=string
TOGGLECASE=string
x=len(string)
count=0
for i in range(0,x):
    if ord(string[i])>=65 and ord(string[i])<=90:
        LCASE=LCASE[:i]+chr(ord(LCASE[i])+32)+LCASE[i+1:]
        TOGGLECASE=TOGGLECASE[:i]+TOGGLECASE[i].lower()+TOGGLECASE[i+1:]
    else:
        TOGGLECASE=TOGGLECASE[:i]+TOGGLECASE[i].upper()+TOGGLECASE[i+1:]
print(LCASE)
print(TOGGLECASE)
