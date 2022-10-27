import csv

def create_file():
    f=open("student.csv","w",newline="")
    stu=csv.writer(f)
    n=int(input("Enter no. of text:"))
    stu.writerow(["Admno","Name","Class","Sec"])
    for i in range(n):
        admno=int(input("Enter admno.:"))
        name=input("Enter name:")
        class_=int(input("Enter class:"))
        sec=input("Enter section:")
        L=[admno,name,class_,sec]
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
    ele=input("Enter admno to be searched:")
    for s in stu:
        print(s,type(s))
        if s[0]==ele:
            print("The desired record is",s)
            break

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
