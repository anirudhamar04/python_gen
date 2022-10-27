L=[[1,2,3],[4,5,6],[7,8,9]]
N=3
for i in range(N):
    rmax=0
    rmin=100
    for j in range(N):
        if(L[i][j]>rmax):
            rmax=L[i][j]
        if (L[i][j]<rmin):
            rmin=L[i][j]

    print(rmin)
    print(rmax)
