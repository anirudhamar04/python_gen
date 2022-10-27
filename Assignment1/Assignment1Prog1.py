def Checkprime(N):
    for i in range(2,N//2+1):
        if N%i==0:
            return True 
    else:
        return False
number=int(input("Enter a number:"))
if Checkprime(number):
    print("Number",number,"is not a prime number")
else:
    print("Number",number,"is a prime number")

