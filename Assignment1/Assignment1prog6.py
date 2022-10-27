N=0
def Create_list(L):
    for i in range(N):
        L[i]=int(input("Enter list element:"))

def fun_search(L,search):
    pos=None
    for i in range(len(L)):
        if L[i]==search:
            pos=i
            break
    return pos

def display_list(L,N):
    print("The elements of the list are ",L,", number of elements =",N)


X=[]
N= int(input("Enter number of elements:"))
X=[0]*N
while True:
    print("1.Create List")
    print("2.Search List")
    print("3.Display List")
    print("4.Quit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        Create_list(X)
    elif choice == 2:
        ele=int(input("Element to be searched:"))
        pos=fun_search(X,ele)
        if pos== None:
            print("The element is not present in the list")
        else:
            print("The element is present in ",pos,"position.")
    elif choice ==3:
        display_list(X,N)
    elif choice == 4:
        break
    else:
        print("Invalid Input")


'''
Output
Enter number of elements:6
1.Create List
2.Search List
3.Display List
4.Quit
Enter your choice:1
Enter list element:56
Enter list element:34
Enter list element:78
Enter list element:12
Enter list element:19
Enter list element:21
1.Create List
2.Search List
3.Display List
4.Quit
Enter your choice:2
Element to be searched:12
The element is present in  3 position.
1.Create List
2.Search List
3.Display List
4.Quit
Enter your choice:2
Element to be searched:22
The element is not present in the list
1.Create List
2.Search List
3.Display List
4.Quit
Enter your choice:3
The elements of the list are  [56, 34, 78, 12, 19, 21] , number of elements = 6
1.Create List
2.Search List
3.Display List
4.Quit
Enter your choice:4
'''





