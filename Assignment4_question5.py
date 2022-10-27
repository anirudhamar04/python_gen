A=[1,2,3,4,5,6,7,8,9]
B=[10,20,30,40,50]
k=0
for i in range(len(B)):
    if k>(len(A)-1):
        A+=[0]*(k-len(A))
        A.insert(k,B[i])
        k+=i+2
    else:    
        A.insert(k,B[i])
        k+=i+2
print(A)
