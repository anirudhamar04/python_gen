def FIBO(N):
    a=1
    b=1
    c=0
    string="The"+str(N)+"terms of the fibonacci series are :"+str(a)+","+str(b)+","
    for i in range(N-2):
        c=a+b
        a=b
        b=c
        string+=str(c)+","
    string=string[:len(string)-2]
    print(string)
    
number=int(input("Enter za number:"))
FIBO(number)
