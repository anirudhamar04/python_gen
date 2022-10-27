A=[]
B=[]
C=[]
M=int(input("Enter no of elements in A:"))
for i in range(M):
    temp=int(input("Enter ele:"))
    A+=[temp]
N=int(input("Enter no of elements in B:"))
for i in range(N):
    temp=int(input("Enter ele:"))
    B+=[temp]
def printlist(A,B,C):
    print(A)
    print(B)
    print(C)
def MIX(A,B,C):
    C+=[0]*(len(A)+len(B))
    even_ele=0
    odd_ele=-1
    for i in A:
        if i%2==0:
            C[even_ele]=i
            even_ele+=1
        else:
            C[odd_ele]=i
            odd_ele-=1
    for i in B:
        if i%2==0:
            C[even_ele]=i
            even_ele+=1
        else:
            C[odd_ele]=i
            odd_ele-=1
MIX(A,B,C)
print("The resultant array C is",C)

'''
Enter no of elements in A:6
Enter ele:3
Enter ele:2
Enter ele:1
Enter ele:7
Enter ele:6
Enter ele:3
Enter no of elements in B:7
Enter ele:9
Enter ele:3
Enter ele:5
Enter ele:6
Enter ele:2
Enter ele:8
Enter ele:10
The resultant array C is [2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3]
'''