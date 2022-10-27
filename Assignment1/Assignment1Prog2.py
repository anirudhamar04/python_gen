def Fact_Num(N):
    fact=1
    for i in range(1,N+1):
        fact*=i
    return fact
Number=int(input("Enter a number:"))
fact=Fact_Num(Number)
print("Factorial of",Number,"is",fact)