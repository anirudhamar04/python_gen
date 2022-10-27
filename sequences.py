maxx=int(input("max="))
i=1
count=1
while i>0:
    
    print((maxx-i)*' ',end='')
    print(i*'* ')
    if i<maxx and count<maxx:
          i+=1
    else:
        i-=1
    count+=1

i=1
count=1
while i>0:
    
    
    print(i*'* ')
    if i<maxx and count<maxx:
          i+=1
    else:
        i-=1
    count+=1
i=1
count=1
while i>0:
    if i==maxx:
        print('*',((maxx+1)-1)*' ','*')
    else:
        print((maxx-i)*' ',end='')
        print(i*'* ')
    if i<maxx and count<maxx:
          i+=1
    else:
        i-=1
    count+=1
i=1
count=1
while i>0:
    if i==3:
        print('*',((maxx+1)-1)*' ','*')
    else:
        
        print(i*'* ')
    if i<maxx and count<maxx:
          i+=1
    else:
        i-=1
    count+=1
