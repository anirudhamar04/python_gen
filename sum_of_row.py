n=int(input('n:'))
grid=[]
sum_row=0
sum_column=0
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
        sum_row+=grid[i][j]
        sum_column+=grid[j][i]
    print ("Sum of",j+1,"row=",sum_row)
    sum_row=0
    print ("Sum of",j+1,"column=",sum_column)
    sum_column=0
