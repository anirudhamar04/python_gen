import csv

def create_file():
    f=open("coun.csv","w",newline="")
    stu=csv.writer(f)
    n=int(input("Enter no. of inputs:"))
    stu.writerow(["Country_id","Country_name","Region_id"])
    for i in range(n):
        admno=input("Enter Country_id:")
        name=input("Enter Country_name:")
        class_=int(input("Enter Region_id:"))
        L=[admno,name,class_]
        stu.writerow(L)
    f.close()

def read_file(fname):
    f=open(fname+".csv","r")
    stu=csv.reader(f)
    for s in stu:
        print(s)


def search_file(fname):
    f=open(fname+".csv","r")
    stu=csv.reader(f)
    ele=input("Enter Country_id to be searched:")
    found=True
    for s in stu:
        if s[0]==ele:
            print("The details of country id",s[0],"is:",s)
            found=False
            break
    if found:
        print("Country_id not found.")
while True:
    print("1.Create file")
    print("2.Display file")
    print("3.Search")
    print("4.Quit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        create_file()
    elif choice == 2:
        fname=input("Enter file name:")
        read_file(fname)
    elif choice == 3:
        fname=input("Enter file name:")
        search_file(fname)
    elif choice == 4:
        break
    else:
        print("Invalid input try again")


'''
1.Create file
2.Display file
3.Search
4.Quit
Enter your choice:1
Enter no. of inputs:5
Enter Country_id:AR
Enter Country_name:Argentina
Enter Region_id:2
Enter Country_id:AU
Enter Country_name:Australia
Enter Region_id:3
Enter Country_id:BE
Enter Country_name:Belgium
Enter Region_id:1
Enter Country_id:BR 
Enter Country_name:Brazil
Enter Region_id:2
Enter Country_id:CA
Enter Country_name:Canada
Enter Region_id:2
1.Create file
2.Display file
3.Search
4.Quit
Enter your choice:2
Enter file name:coun
['Country_id', 'Country_name', 'Region_id']
['AR', 'Argentina', '2']
['AU', 'Australia', '3']
['BE', 'Belgium', '1']
['BR ', 'Brazil', '2']
['CA', 'Canada', '2']
1.Create file
2.Display file
3.Search
4.Quit
Enter your choice:3
Enter file name:coun
Enter Country_id to be searched:BR 
The details of country id BR  is: ['BR ', 'Brazil', '2']
1.Create file
2.Display file
3.Search
4.Quit
Enter your choice:3
Enter file name:coun
Enter Country_id to be searched:AU
The details of country id AU is: ['AU', 'Australia', '3']
1.Create file
2.Display file
3.Search
4.Quit
Enter your choice:3
Enter file name:coun
Enter Country_id to be searched:IN
Country_id not found.
1.Create file
2.Display file
3.Search
4.Quit
Enter your choice:4
'''