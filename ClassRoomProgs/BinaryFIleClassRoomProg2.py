import pickle
import os
def create_file():
    n= int(input("Enter no. of entries:"))
    stu_file=open("Stu1.dat","wb")
    st={}
    for i in range(n):
        ad=int(input("Enter admno:"))
        nm=input("Enter the name:")
        cl=int(input("Enter class:"))
        sec=input("Enter sections:")
        st["admno"]=ad
        st["name"]=nm
        st["class"]=cl
        st["section"]=sec
        pickle.dump(st,stu_file)
    stu_file.close()

def read_file():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","rb")
    temp={}
    try:
        while True:
            temp=pickle.load(stu_file)
            print(temp)
    except EOFError:
        print("Closing file...")
        stu_file.close()

def app_bin():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","ab")
    n=int(input("Enter no. of entries:"))
    st={}
    for i in range(n):
        ad=int(input("Enter admno:"))
        nm=input("Enter the name:")
        cl=int(input("Enter class:"))
        sec=input("Enter sections:")
        st["admno"]=ad
        st["name"]=nm
        st["class"]=cl
        st["section"]=sec
        pickle.dump(st,stu_file)
    stu_file.close()

def updt_bin():
    found=0
    fname=input("Enter file name:")
    f=open(fname+".dat","rb+")
    admno=int(input("Enter admno to be updated:"))
    name=input("New name:")

    try:
        ptr=0
        while True:
            st=dict()
            pointer=f.tell()
            f.seek(ptr)
            st=pickle.load(f)
            if st["admno"]==admno:
                st["name"]=name
                f.seek(pointer)
                pickle.dump(st,f)
                found=1
                break
            ptr=f.tell()
    except EOFError:
        if found==1:
            print("Record found and updated.")
        else:
            print("Record not found.")
    f.seek(0)
    f.close()


while True:
    print("1. Create File:")
    print("2. Read FIle")
    print("3. Append File:")
    print("4. Update record:")
    print("5. Quit")
    choice=input("Enter choice:")
    if choice == "1":
        create_file()
    elif choice=="2":
        read_file()
    elif choice=="3":
        app_bin()
    elif choice == "4":
        updt_bin()
    elif choice == "5":
        break
    else:
        print("Invalid input")



'''
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:1
Enter no. of entries:3
Enter admno:46
Enter the name:nah
Enter class:5
Enter sections:E
Enter admno:5674
Enter the name:Aniru
Enter class:12
Enter sections:A
Enter admno:3456
Enter the name:nah
Enter class:6
Enter sections:e
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:2
Enter file name:Stu1
{'admno': 46, 'name': 'nah', 'class': 5, 'section': 'E'}
{'admno': 5674, 'name': 'Aniru', 'class': 12, 'section': 'A'}
{'admno': 3456, 'name': 'nah', 'class': 6, 'section': 'e'}
Closing file...
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:3
Enter file name:Stu1
Enter no. of entries:2
Enter admno:3456
Enter the name:Sup
Enter class:12
Enter sections:C
Enter admno:3478
Enter the name:ajid
Enter class:11
Enter sections:D
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:2
Enter file name:Stu1
{'admno': 46, 'name': 'nah', 'class': 5, 'section': 'E'}
{'admno': 5674, 'name': 'Aniru', 'class': 12, 'section': 'A'}
{'admno': 3456, 'name': 'nah', 'class': 6, 'section': 'e'}
{'admno': 3456, 'name': 'Sup', 'class': 12, 'section': 'C'}
{'admno': 3478, 'name': 'ajid', 'class': 11, 'section': 'D'}
Closing file...
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:4
Enter file name:Stu1
Enter admno to be updated:5674
New name:Anirudh
Record found and updated.
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:2
Enter file name:Stu1
{'admno': 46, 'name': 'nah', 'class': 5, 'section': 'E'}
{'admno': 5674, 'name': 'Anirudh', 'class': 12, 'section': 'A'}
{'admno': 3456, 'name': 'nah', 'class': 6, 'section': 'e'}
{'admno': 3456, 'name': 'Sup', 'class': 12, 'section': 'C'}
{'admno': 3478, 'name': 'ajid', 'class': 11, 'section': 'D'}
Closing file...
1. Create File:
2. Read FIle
3. Append File:
4. Update record:
5. Quit
Enter choice:5
'''