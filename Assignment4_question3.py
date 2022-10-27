days=int(input("Number of days :"))
Temp=[]
count=0
k=0
for i in range(days):
    L=float(input("Enter the element"))
    Temp+=[L]
for i in range(len(Temp)):
    if Temp[i]<0:
        temp=Temp[i]
        for j in range(i,k-1,-1):
            Temp[j]=Temp[j-1]
        Temp[k]=temp
        k+=1
print("The elements after shifting are:",Temp)
   
