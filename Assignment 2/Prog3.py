def sum_series(N):
    if N==1:
        return 1
    elif N%2==0:
        return -1/N+sum_series(N-1)
    else:
        return 1/N+sum_series(N-1)

N=int(input("N="))
print("The sum of the 4 terms are", sum_series(4))

'''
N=4
The sum of the 4 terms are 0.5833333333333333
'''