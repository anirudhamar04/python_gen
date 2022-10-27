X=[3,6,6,7,8,1,5,6,5,3,5]
x=0
for i in X:
    x=0
    count=X.count(i)
    if count>1:
        while x<count-1:
            X.remove(i)
            i+=1
    
print(X)
