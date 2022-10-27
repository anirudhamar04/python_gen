x=int(input("Enter a number:"))
n=int(input("Enter a number:"))
S=1
fact=1
sign=-1
for i in range(2,2*n+1,2):
    fact=fact*i*(i-1)
    exp=((x**(i/2))/fact)*sign
    S+=exp
    sign*=-1
print('The sum of the series =',S)
