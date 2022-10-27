n=int(input("Enter no. of elements:"))
L=[]
unique=[]
repeated=[]
for x in range(n):
    l=int(input("Enter element:"))
    L+=[l]
for i in L:
    count=0
    for j in L:
        if i==j:
            count+=1

    if count==1:
        unique+=[i]
    elif count>1 and i not in repeated:
        repeated+=[i]
print("Unique  :",unique)
print("Repeated:",repeated)
