n1=int(input("n1?"))
n2=int(input("n2?"))
sum_ = 0
for x in range ( n1,n2+1):
    if x!=1:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x,end=',')
            sum_+=1
print('Total no. of prime no.s =',sum_)
