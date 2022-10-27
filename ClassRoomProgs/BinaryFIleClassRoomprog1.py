import pickle
import os
def create_file():
    n= int(input("Enter no. of entries:"))
    stu_file=open("Stu.dat","wb")
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

def search_file():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","rb")
    temp={}
    chk=0
    try:
        while True:
            temp=pickle.load(stu_file)
            if temp["name"][0]=="S":
                print(temp)
                chk+=1
    except EOFError:
        print("Closing file...")
        stu_file.close()
    if chk==0:
        print("Data not found")

def delete():
    fname=input("Enter name of file:")
    f1=open(fname+".dat","rb")
    f2=open("copy.dat","wb")
    try:
        while True:
            temp=pickle.load(f1)
            if temp["section"]!="T":
                pickle.dump(temp,f2)
                
    except EOFError:
        print("Closing file...")
        f1.close()
        f2.close()
    os.remove(fname+".dat")
    os.rename("copy.dat",fname+".dat")


while True:
    print("1. Create File:")
    print("2. Read FIle")
    print("3. Search File:")
    print("4. Delete record:")
    print("5. Quit")
    choice=input("Enter choice:")
    if choice == "1":
        create_file()
    elif choice=="2":
        read_file()
    elif choice=="3":
        search_file()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Invalid input")


'''
1. Create File:
2. Read FIle
3. Search File:
4. Delete record:
5. Quit
Enter choice:1
Enter no. of entries:4
Enter admno:1234
Enter the name:Saturday
Enter class:12
Enter sections:T
Enter admno:9678
Enter the name:Anirudh
Enter class:12
Enter sections:A
Enter admno:76
Enter the name:Sapling
Enter class:2 
Enter sections:T
Enter admno:5674
Enter the name:jsd
Enter class:3
Enter sections:A
1. Create File:
2. Read FIle
3. Search File:
4. Delete record:
5. Quit
Enter choice:2
Enter file name:Stu
{'admno': 1234, 'name': 'Saturday', 'class': 12, 'section': 'T'}
{'admno': 9678, 'name': 'Anirudh', 'class': 12, 'section': 'A'}
{'admno': 76, 'name': 'Sapling', 'class': 2, 'section': 'T'}
{'admno': 5674, 'name': 'jsd', 'class': 3, 'section': 'A'}
Closing file...
1. Create File:
2. Read FIle
3. Search File:
4. Delete record:
5. Quit
Enter choice:3
Enter file name:Stu
{'admno': 1234, 'name': 'Saturday', 'class': 12, 'section': 'T'}
{'admno': 76, 'name': 'Sapling', 'class': 2, 'section': 'T'}
Closing file...
1. Create File:
2. Read FIle
3. Search File:
4. Delete record:
5. Quit
Enter choice:4
Enter name of file:Stu
Closing file...
1. Create File:
2. Read FIle
3. Search File:
4. Delete record:
5. Quit
Enter choice:2
Enter file name:Stu
{'admno': 9678, 'name': 'Anirudh', 'class': 12, 'section': 'A'}
{'admno': 5674, 'name': 'jsd', 'class': 3, 'section': 'A'}
Closing file...
1. Create File:
2. Read FIle
3. Search File:
4. Delete record:
5. Quit
Enter choice:5
'''