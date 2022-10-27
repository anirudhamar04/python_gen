def push(Op_data):
    global top
    operator=input("Enter Character:")
    PrecedenceOrder=int(input("Enter Precedence Order:"))
    elem=[operator, PrecedenceOrder]
    Op_data.append(elem)
    top=len(Op_data)-1

def pop(Op_data):
    global top
    if Op_data!=[]:
        Op_data.pop()
        top=len(Op_data)-1
        print("Stack element popped")
    else:
        print("Underflow")
        top=None

def peek(Op_data):
    if top==None or top==-1:
        print("Stack is empty")
    else:
        print("Operator  Precedence Order")
        for i in range(len(Op_data)-1,-1,-1):
            print(Op_data[i])

Op_data=[]
top=None
while True:
    print("1.Display stack")
    print("2.Push stack")
    print("3.Pop Stack")
    print("4.Quit")
    ch=input("Enter your choice:")
    if ch=="1":
        peek(Op_data)
    elif ch=="2":
        push(Op_data)
    elif ch=="3":
        pop(Op_data)
    elif ch=="4":
        break
    else:
        print("Invalid input")
'''

1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter Character:+
Enter Precedence Order:3
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:1
Operator  Precedence Order
['+', 3]
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
Enter your choice:2
Enter Character:*
Enter Precedence Order:2
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter Character:/
Enter Precedence Order:2
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter Character:-
Enter Precedence Order:3
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:1
Operator  Precedence Order
['-', 3]
['/', 2]
['*', 2]
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter Character:) 
Enter Precedence Order:5
1.Display stack
2.Push stack
3.Pop Stack
4.Quit
Enter your choice:2
Enter Character:(
Enter Precedence Order:6
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
Enter your choice:3
Stack element popped
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
Operator  Precedence Order
['/', 2]
['*', 2]
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
Enter your choice:3
Stack element popped
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
Enter your choice:4
'''