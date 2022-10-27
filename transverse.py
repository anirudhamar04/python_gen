A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[0,0,0],[0,0,0],[0,0,0]]
n=3
for x in range(n):
    for y in range(n):
        B[y][x]=A[x][y]




for i in range(n):
    for j in range(n):
        print(A[i][j],end="")
    print()

print() 
for i in range(n):
    for j in range(n):
        print(B[i][j],end="")
    print()
