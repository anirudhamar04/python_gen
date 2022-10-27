'''
#question1
for i in range(2,21,2):
    print(i)

#question2
print("Natural no.s b/w 10 to 1")
for i in range(10,0,-1):
    print(i)

#question3
n = int(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

for i in range(105,999,5):
    if not(i%2==0):
        print(i)

#question4
n = int(input("Enter the number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)


#question5
s=0
for i in range(1,11):
    print("Enter number",i)
    n = int(input())
    if n%2==0:
        s=s+n

print(s)

#question6
n=int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
   fact=fact*i
print("Factorial of",n,"is",fact)
'''
#question7
n=int(input("Enter the number of digits in the series:"))
a=0
b=1
print(a,b,end=' ')
for i in range(n-2):
      c=a+b
      print(c,end=' ')
      a=b
      b=c
      
