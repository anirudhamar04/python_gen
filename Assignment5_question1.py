n=int(input("Enter number of times it much be repeated:"))
Str="abcdeghijklmnopqrstuvwxyz"
Temp=""
A= tuple()
B= tuple()
for i in Str:
    Temp+=i
    A+=(Temp,)
print("A =",A)
if n>9:
    n=9
Temp=""
for j in range(1,n+1):
    Temp=str(j)*j
    B+=(Temp,)
print()
print()
print("B=",B)
