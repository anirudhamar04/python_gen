def fun_sort(L):
    for i in range(len(L)):
        key=L[i]
        j=i-1
        while j>=0 and key<L[j]:
            L[j+1]=L[j]
            j=j-1
        L[j+1]=key
    
def fun_ins(L,ins):
    pos=len(L)
    for i in range(len(L)):
        if L[i]>ins:
            pos=i
            break
    L+=[pos]
    for i in range(len(L)-2,pos-1,-1):
        L[i+1]=L[i]
    L[pos]=ins
    

def fun_del(L,num):
    x=len(L)
    i=0
    chk=0
    while(i<=x-1):
        if num==L[i]:
            j=i
            while (j<x-1):
                L[j]=L[j+1]
                j=j+1
            L.pop()
            chk=1
            x=len(L)
            i=i-1
        i=i+1
    if chk==0:
        print("Element not found.")
    else:
        print("Element deleted.")
    return L

def fun_rev(L,n):
    for i in range(n//2):
        L[i],L[-i-1] = L[-i-1],L[i]
    return L

def fun_disp(L):
    x=len(L)
    for i in range(x):
        print(L[i],end=",")
    print()
n=int(input("Number of elemnts in list:"))
L=[]
for i in range(n):
    ele=int(input("Enter element:"))
    L+=[ele]

while True:
    print("1.Sort List")
    print("2.Insert List element")
    print("3.Delete list element")
    print("4.Reverse List")
    print("5.Display list")
    print("6.Quit")
    choice=input("Enter your choice:")
    if choice == "1":
        fun_sort(L)
    elif choice == "2":
        ins=int(input("Enter element to be inserted:"))
        fun_ins(L,ins)
    elif choice == "3":
        num=int(input("Enter element to be deleted:"))
        L=fun_del(L,num)
    elif choice == "4":
        L=fun_rev(L)
    elif choice == "5":
        fun_disp(L)
    elif choice == "6":
        break
    else:
        print("Invalid input try again")


'''
Number of elemnts in list:6
Enter element:56
Enter element:34
Enter element:78
Enter element:12
Enter element:19
Enter element:21
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:1
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:5
12,19,21,34,56,78,
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:2
Enter element to be inserted:100
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:5
12,19,21,34,56,78,100,
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:3
Enter element to be deleted:100
Element deleted.
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:5
12,19,21,34,56,78,
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:3
Enter element to be deleted:200
Element not found.
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:4
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:5
78,56,34,21,19,
1.Sort List
2.Insert List element
3.Delete list element
4.Reverse List
5.Display list
6.Quit
Enter your choice:6
'''