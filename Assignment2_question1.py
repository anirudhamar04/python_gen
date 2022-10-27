n=int(input("Enter a number:"))
rem=0
rev=0
flag=0
n_=n
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print(n,'is a composite number')
else:
    for i in range(len(str(n))):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if n_==rev:
        print(n_,'is a prime palindrome')
    else:
        print(n_,'is a prime number')
