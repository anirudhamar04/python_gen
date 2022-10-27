x=int(input("Enter a number:"))
n=int(input("Enter a number:"))
s=0
sign=-1
for i in range(1,n+1,2):
    sign*=-1
    t=((x**i/i))*sign
    s+=t
print('The sum of the series where x=',x,'and n=',n,'is',s)
