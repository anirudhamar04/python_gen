n=int(input("Number of tuples:"))
tup=tuple()
finalTup=tuple()
for i in range(n):
    tempTup=tuple()
    for j in range(2):
        k=int(input("Enter the number:"))
        tempTup+=(k,)
    tup+=(tempTup,)
for x in range(len(tup)):
    if tup[x][0]-tup[x][1]==2 or tup[x][0]-tup[x][1]==-2:
        flag1=0
        flag2=0
        if tup[x][0]>tup[x][1]:
            for y in range(2,tup[x][0]//2):
                if tup[x][0]%y==0:
                    flag1=1
                if tup[x][0]%y==0:
                    flag2=1
        elif tup[x][0]<tup[x][1]:
            for y in range(2,tup[x][1]//2):
                if tup[x][0]%y==0:
                    flag1=1
                if tup[x][1]%y==0:
                    flag2=1
        if flag1==0 and flag2==0:
                finalTup+=(tup[x],)
print("Twin Primes are :")
for i in finalTup:
    print(i)

