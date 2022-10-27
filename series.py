N=int(input("Enter the value:"))
string='1'
series=0
for i in range (1,N):
    series+=i
    if i>1:
        string+='+'+str(i)
    print (string,'=',series)
