L=eval(input("Enter a list of natural no.s:"))

for i in L:
    flag=0
    if i !=1:
        for j in range(2,i//2):
            if i%j==0:
                flag+=1
            
        if 
