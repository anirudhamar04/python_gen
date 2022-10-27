n=int(input("Number of elements:"))
L=[]
for i in range(n):
    num=int(input("Enter the element:"))
    L+=[num]
num=int(input("No. of no.s to be insterted:"))

for x in range(num):
    k=len(L)
    insert=int(input("Enter no. to be inserted:"))
    L+=[insert]
    for y in range(-2,((-1*n)-2),-1):
        if L[y]>L[k]:
            temp=L[y]
            L[y]=L[k]
            L[k]=temp
            k-=1
    print("List after insterting",insert,"is",L)
