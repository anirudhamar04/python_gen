#q1

L=eval(input("Enter the tuple:"))
sum_=0


for i in L:
    sum_+=i

avg=sum_/len(L)
print("Avg=:",avg)
#minMax
Max=L[0]
Min=L[0]

for i in L:
    if i>Max:
        Max=i
    elif i<Min:
        Min=i
print("Max=",Max,"Min=",Min)
