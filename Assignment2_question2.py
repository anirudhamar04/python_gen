n=int(input("Enter a number:"))
a=0
b=1
c=1
print(a,b,c,end=' ')
for i in range(1,n-2):
    d=a+b+c
    print(d,end=' ')
    a=b
    b=c
    c=d
