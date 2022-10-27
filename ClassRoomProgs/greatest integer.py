def t(a,b,c):
    L=(a,b,c)
    max_=0
    for i in L:
        if i>max_:
            max_=i
    return max_
x=t(11,9,10)
print(x)
