'''
l =[0,2,3,0,4,5,0,6]
j=0
for i in range(len(l)):
    if l[i]!=0:
        l[j]=l[i]
        j+=1
for i in range(j,len(l)):
    l[i]=0

print(l)

l=[1,2,3,4,5]
n=5
for i in range (0,n):
    first=l[0]
    for j in range(0,len(l)-1):
        l[j]=l[j+1]
    l[len(l)-1]=first
    print(l)
'''
l=[1,2,3,4,5]
n=5
for i in range (0,n):
    last=l[len(l)-1]
    for j in range(len(l)-1,0,-1):
        l[j]=l[j-1]
    l[0]=last
    print(l)

