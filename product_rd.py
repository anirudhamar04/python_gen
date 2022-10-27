n=int(input('n:'))
grid=[]
sum_ld=0
product_rd=1
for i in range (n):
    col=[]
    for j in range(n):
        col+=[0]
    grid+=[col]
print(grid)

for i in range(n):
    for j in range(n):
        print ("Enter in row:",i+1,"Column:",j+1)
        grid[i][j]=int(input())

for i in range(n):
    for j in range(n):
        print(grid[i][j],end="")
    print()

for i in range(n):
    for j in range(n):
        if i==j:
            sum_ld+=grid[i][j]
            print(grid[i][j],end=' ')
        if i+j==n-1:
            product_rd*=grid[i][j]
            print(grid[i][j])
print("Sum of left diagnol=",sum_ld)
print("product of left diagnol=",product_rd)
