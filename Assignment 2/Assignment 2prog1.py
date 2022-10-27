def sort(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]

def bin_search(lb,ub,data,L):
    global mid
    mid=(lb+ub)//2
    if lb>ub:
        return None
    if data==L[mid]:
        return mid
    
    elif data>L[mid]:
        return bin_search(mid+1,ub,data,L)
    elif data<L[mid]:
        return bin_search(lb,mid-1,data,L)
    

L= []
n=int(input("Enter number of elements in the list:"))
for i in range(n):
    ele=int(input("Enter element:"))
    L+=[ele]
while True:
    print("1. Sort List")
    print("2. Search List")
    print("3. Quit")
    ch=input("Enter your choice:")
    if ch=="1":
        sort(L)
        print("The elements after sorting in the ascending order are:",L)
    elif ch=="2":
        ele=int(input("Element to be searched:"))
        lb=0
        ub=len(L)-1
        pos=bin_search(lb,ub,ele,L)
        if pos!=None:
            print("The element is present in position",pos+1)
        elif pos==None:
            print("Element not found")
    elif ch=="3":
        break
    else:
        print("Invalid Input")
'''
Enter number of elements in the list:6
Enter element:56
Enter element:34
Enter element:78
Enter element:12
Enter element:19
Enter element:21
1. Sort List
2. Search List
3. Quit
Enter your choice:1
The elements after sorting in the ascending order are: [12, 19, 21, 34, 56, 78]
1. Sort List
2. Search List
3. Quit
Enter your choice:2
Element to be searched:34
The element is present in position 4
1. Sort List
2. Search ListEnter number of elements in the list:6
Enter element:56
Enter element:34
Enter element:78
Enter element:12
Enter element:19
Enter element:21
1. Sort List
2. Search List
3. Quit
Enter your choice:1
The elements after sorting in the ascending order are: [12, 19, 21, 34, 56, 78]
1. Sort List
2. Search List
3. Quit
Enter your choice:2
Element to be searched:34
The element is present in position 4
1. Sort List
2. Search List
3. Quit
Enter your choice:2
Element to be searched:43
Element not found
1. Sort List
2. Search List
3. Quit
Enter your choice:3
'''
