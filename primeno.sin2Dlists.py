L=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for i in range(n):
    for j in range(n):
        for x in range(2,L[i][j]):
            if L[i][j]%x==0:
                break
        else:
            L[i][j]='*'
        
       


for i in range(n):
    for j in range(n):
        print(L[i][j],end="")
    print()
                
        
            
