import math
#question1
num = input("Enter a number:")
l=len(num)
for i in range(l):
    print("Digit",i+1,":",num[i])
    print("Square of digit",i+1,":",(int(num[i]))**2)

#question2
even = 0
odd = 0
for i in range(1,11):
    if (i%2==0):
        even+=i
    else:
        odd +=i
        
print(even,odd)

#question3

n = int(input("Enter a number:"))
d=0
s=0
l= len(str(n))
temp = n
for i in range(l):
        d=n%10
        s+=math.pow(d,l)
        n=n/10
if s == temp:
        print(temp,'is a armstrong no.')
else:
        print(temp,'is not a armstrong no.')
#queston4
n=int(input("Enter a number:"))
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i

if s==n:
        print(n,"is a perfect no.")
else:
        print(n,"is not a perfect no.")

#question5
x= int(input("Enter a numer:"))
y= int(input("Enter a numer:"))
if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller//2+1):
    if (x%i==0 and y%i==0):
        hcf=i
lcm=x*y/hcf
print("LCM =",lcm,"HCF=",hcf)

#question6
min=100
max=0
for i in range(1,11):
   if i<min:
      min=i
   else:
      max=i
print("minimum:",min)
print("maximum:",max)
