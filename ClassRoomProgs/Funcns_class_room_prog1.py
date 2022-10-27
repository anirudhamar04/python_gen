def TOT(N):
    Sum=0
    for i in range(N+1):
        Sum+=i

    return Sum

No=int(input("Enter the number:"))
Sum=TOT(No)
print(Sum)