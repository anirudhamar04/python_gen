num=int(input("Enter no. to be removed:"))
X=[3,6,6,7,8,1,5,6,5,3,5]
i=0
while i<len(X):
    if X[i]==num:
        X=X[:i]+X[(i+1):]
        i-=1
    i+=1
print(X)
num2=int(input("Enter no. to be removed:5"))
d=X.count(num2)
y=-1
while d>1:
    if X[y]==num2:
        X.pop(y)
        d-=1
    y-=1
    
print(X)
