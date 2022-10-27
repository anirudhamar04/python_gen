def push(stulist):
    global top
    adm=int(input("Enter admno:"))
    nam=input("Enter name:")
    elem=[adm,nam]
    stulist.append(elem)
    top=len(stulist)-1

def pop(stulist):
    global top
    if stulist!=[]:
        stulist.pop()
        top=len(stulist)-1
        print("Stack element popped")
    else:
        print("Underflow")
        top=None

def peek(stulist):
    if top==None:
        print("Stack is empty")
    else:
        for i in range(len(stulist)-1,-1,-1):
            print(stulist[i])

stulist=[]
top=None
while True:
    print("1.Display stack")
    print("2.Push stack")
    print("3.Pop Stack")
    print("4.Quit")
    ch=input("Enter your choice:")
    if ch=="1":
        peek(stulist)
    elif ch=="2":
        push(stulist)
    elif ch=="3":
        pop(stulist)
    elif ch=="4":
        break
    else:
        print("Invalid input")


'''
1.Display stack
2.Push stack      
3.Pop Stack       
4.Quit
Enter your choice:1
Stack is empty 
1.Display stack
2.Push stack   
3.Pop Stack    
4.Quit
Enter your choice:2
Enter admno:5674
Enter name:anirudh
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter admno:38902
Enter name:jmld
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter admno:39
Enter name:xoia
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:1
[39, 'xoia']
[38902, 'jmld']
[5674, 'anirudh']
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:3
Stack element popped
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:1
[38902, 'jmld']
[5674, 'anirudh']
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:3
Stack element popped
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:1
[5674, 'anirudh']
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:3
Stack element popped
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:1
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:3
Underflow
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:4
'''