l=2
r=3
grid=[]

for i in range (l):
    col=[]
    for j in range(r):
        col+=[0]
    grid+=[col]
print(grid)

for i in range(l):
    for j in range(r):
        print ("Enter in row:",i+1,"Column:",j+1)
        grid[i][j]=int(input())
       

for i in range(l):
    for j in range(2):
        print(grid[i][j],end="")
    print()

print("Sum of all elements =",sum_)

