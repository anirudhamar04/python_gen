N=0
def create_list(L):
    print(L)
    for i in range(N):
        L[i]=int(input("Enter list elements:"))

def swap_list(L):
    for i in range(0,N-1,2):
        L[i],L[i+1]=L[i+1],L[i]
    print(L)

def sec_max(L):
    max,sec_max=L[0],L[0]
    for ele in L:
        if ele>=max:
            max=ele
        else:
            sec_max=ele
    for ele in L:
        if ele>=sec_max and ele!= max:
            sec_max=ele
    return sec_max

def display_list(L):
    print(L)

#main
X=[]
N=int(input("Enter no. of elements:"))
X=[0]*N

while True:
    print("1.Create List")
    print("2.Display List")
    print("3.Swap List")
    print("4.Find Sec max")
    print("5.Quit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        create_list(X)
    elif choice == 2:
        display_list(X)
    elif choice == 3:
        swap_list(X)
    elif choice == 4:
        print(sec_max(X))
    elif choice == 5:
        break
    else:
        print("Invalid input try again")
print("Quitting...")

'''Output:
Enter no. of elements:5
1.Create List
2.Display List
3.Swap List
4.Find Sec max
5.Quit
Enter your choice:1
[0, 0, 0, 0, 0]
Enter list elements:29
Enter list elements:30
Enter list elements:40
Enter list elements:21
Enter list elements:48
1.Create List
2.Display List
3.Swap List
4.Find Sec max
5.Quit
Enter your choice:2
[29, 30, 40, 21, 48]
1.Create List
2.Display List
3.Swap List
4.Find Sec max
5.Quit
Enter your choice:3
[30, 29, 21, 40, 48]
1.Create List
2.Display List
3.Swap List
4.Find Sec max
5.Quit
Enter your choice:4
40
'''