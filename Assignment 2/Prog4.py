def tribo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return 1
    else:
        return tribo(n-1)+tribo(n-2)+tribo(n-3)

n=int(input("N="))
print("The first",n,"terms of the tribonacci series are: ",end="")
for i in range(1,n+1):
    if i==n:
        print(tribo(i))
    else:
        print(tribo(i),end=",")

'''
N=5
The first 5 terms of the tribonacci series are: 0,1,1,2,4
'''