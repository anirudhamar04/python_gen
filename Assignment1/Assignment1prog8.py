def Create_list():
    n=int(input("Enter the order of the list:"))
    List=[]
    for i in range(n):
        Col=[]
        for j in range(n):
            print("Enter element for row",i+1,"column",j+1,":")
            temp=int(input())
            Col+=[temp]
        List+=[Col]
    
    return List
    
def Display_List(List):
    n=len(List)
    for i in range(n):
        for j in range(n):
            print(List[i][j],end=" ")
        print("\n",end="")

def diagnol_ele(List):
    n=len(List)
    prod_left=1
    prod_right=1
    for i in range(n):
        for j in range(n):
            if i==j:
                prod_left*=List[i][j]
                prod_right*=List[n-1-i][j]
    print("Product of the left diagnol=",prod_left)
    print("Product of the right diagnol=",prod_right)


def prod_row(List):
    product=1
    n=len(List)
    for i in range(n):
        largestele=0
        for j in range(n):
            if List[i][j]>largestele:
                largestele=List[i][j]
        product*=largestele
    return product



while True:
    print("1.Create List:")
    print("2.Display List")
    print("3.Product of diagnols")
    print("4.Produc row")
    print("5.Quit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        L=Create_list()
    elif choice==2:
        Display_List(L)
    elif choice==3:
        diagnol_ele(L)
    elif choice==4:
        print("The product of the largest element of each row =",prod_row(L))
    elif choice==5:
        break
    else:
        print("Invalid Input")



'''
Output
1.Create List:
2.Display List
3.Product of diagnols
4.Produc row
5.Quit
Enter your choice:1
Enter the order of the list:3
Enter element for row 1 column 1 :
2
Enter element for row 1 column 2 :
1
Enter element for row 1 column 3 :
1
Enter element for row 2 column 1 :
3
Enter element for row 2 column 2 :
1
Enter element for row 2 column 3 :
2
Enter element for row 3 column 1 :
1
Enter element for row 3 column 2 :
1
Enter element for row 3 column 3 :
2
1.Create List:
2.Display List
3.Product of diagnols
4.Produc row
5.Quit
Enter your choice:2
2 1 1 
3 1 2
1 1 2
1.Create List:
2.Display List
3.Product of diagnols
4.Produc row
5.Quit
Enter your choice:3
Product of the left diagnol= 4
Product of the right diagnol= 1
1.Create List:
2.Display List
3.Product of diagnols
4.Produc row
5.Quit
Enter your choice:4
The product of the largest element of each row = 12
1.Create List:
2.Display List
3.Product of diagnols
4.Produc row
5.Quit
Enter your choice:5
'''