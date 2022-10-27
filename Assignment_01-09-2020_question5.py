n1=int(input("Enter lower limit:"))
n2=int(input("Enter upper limit:"))
sum_= 0
 
for x in range(n1,n2+1):
    if x>1:
        for n in range(2,x):
            if (x%n) == 0:
                break
            else:
                print(x,end=',')
                sum_= sum_+1
print(sum_)
