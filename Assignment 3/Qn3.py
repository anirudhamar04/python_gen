import pickle
import os

def create_file():
    n= int(input("Enter no. of entries:"))
    stu_file=open("cetrk.dat","wb")
    st={}
    for i in range(n):
        ad=int(input("Enter Reg_no:"))
        nm=input("Enter the Name:")
        cl=int(input("Enter Rank:"))
        if cl <=100:
            sec="Computer Science"
        elif cl <=200:
            sec="Electronics"
        elif cl<=300:
            sec="Telecommunications"
        else:
            sec="NO ALLOTMENT"
        st["Reg_no"]=ad
        st["Name"]=nm
        st["Rank"]=cl
        st["SubCode"]=sec
        pickle.dump(st,stu_file)
    stu_file.close()

def read_file():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","rb")
    temp={}
    print("Reg_No."+3*" "+"Name"+6*" "+"Rank"+6*" "+"SubCode")
    try:
        while True:
            temp=pickle.load(stu_file)
            for i in temp:
                print(str(temp[i])+(10-len(str(temp[i])))*" ",end="")
            print()
    except EOFError:
        print("Closing file...")
        stu_file.close()

def app_bin():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","ab")
    n=int(input("Enter no. of entries:"))
    st={}
    for i in range(n):
        ad=int(input("Enter Reg_no:"))
        nm=input("Enter the name:")
        cl=int(input("Enter rank:"))
        if cl<=100:
            sec="Computer Science"
        elif cl<=200:
            sec="Electronics"
        elif cl<=300:
            sec="Telecommmunications"
        else:
            sec="NO ALLOTMENT"
        st["Reg_no"]=ad
        st["Name"]=nm
        st["Rank"]=cl
        st["SubCode"]=sec
        pickle.dump(st,stu_file)
    stu_file.close()

def copy_file():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","rb")
    f=open("cet.dat","wb")
    temp={}
    try:
        while True:
            temp=pickle.load(stu_file)
            if temp["Rank"]<=1000:
                pickle.dump(temp,f)
    except EOFError:
        stu_file.close()
        f.close()



def delete():
    fname=input("Enter name of file:")
    f1=open(fname+".dat","rb")
    f2=open("copy.dat","wb")
    try:
        while True:
            temp=pickle.load(f1)
            if temp["Rank"]<=1500:
                pickle.dump(temp,f2)
                
    except EOFError:
        print("Closing file...")
        f1.close()
        f2.close()
    os.remove(fname+".dat")
    os.rename("copy.dat",fname+".dat")

while True:
    print("1. Create file:")
    print("2. Read file:")
    print("3. Append entries:")
    print("4. Copy file:")
    print("5.Delete entries:")
    print("6. Quit")
    choice=input("Enter your Choice:")
    if choice == "1":
        create_file()
    elif choice=="2":
        read_file()
    elif choice=="3":
        app_bin()
    elif choice == "4":
        copy_file()
    elif choice == "5":
        delete()
    elif choice=="6":
        break
    else:
        print("Invalid input")

'''
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:1
Enter no. of entries:5
Enter Reg_no:1001
Enter the Name:Vinay
Enter Rank:2265
Enter Reg_no:1000
Enter the Name:Rahul
Enter Rank:150
Enter Reg_no:1007
Enter the Name:Vrinda
Enter Rank:1519
Enter Reg_no:1006
Enter the Name:Megha
Enter Rank:320
Enter Reg_no:1333
Enter the Name:Vikas
Enter Rank:1300
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:2
Enter file name:cetrk
Reg_No.   Name      Rank      SubCode
1001      Vinay     2265      NO ALLOTMENT
1000      Rahul     150       Electronics
1007      Vrinda    1519      NO ALLOTMENT
1006      Megha     320       NO ALLOTMENT
1333      Vikas     1300      NO ALLOTMENT
Closing file...
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:3
Enter file name:cetrk
Enter no. of entries:3
Enter Reg_no:1679
Enter the name:Sumith
Enter rank:1700
Enter Reg_no:2435
Enter the name:Ramesh
Enter rank:56
Enter Reg_no:1345
Enter the name:Apoorva
Enter rank:344
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:2
Enter file name:cetrk
Reg_No.   Name      Rank      SubCode
1001      Vinay     2265      NO ALLOTMENT
1000      Rahul     150       Electronics
1007      Vrinda    1519      NO ALLOTMENT
1006      Megha     320       NO ALLOTMENT
1333      Vikas     1300      NO ALLOTMENT
1679      Sumith    1700      NO ALLOTMENT
2435      Ramesh    56        Computer Science
1345      Apoorva   344       NO ALLOTMENT
Closing file...
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:4
Enter file name:cetrk
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:2
Enter file name:cet
Reg_No.   Name      Rank      SubCode
1000      Rahul     150       Electronics
1006      Megha     320       NO ALLOTMENT
2435      Ramesh    56        Computer Science
1345      Apoorva   344       NO ALLOTMENT
Closing file...
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:5
Enter name of file:cetrk
Closing file...
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:2
Enter file name:cetrk
Reg_No.   Name      Rank      SubCode
1000      Rahul     150       Electronics
1006      Megha     320       NO ALLOTMENT
1333      Vikas     1300      NO ALLOTMENT
2435      Ramesh    56        Computer Science
1345      Apoorva   344       NO ALLOTMENT
Closing file...
1. Create file:
2. Read file:
3. Append entries:
4. Copy file:
5.Delete entries:
6. Quit
Enter your Choice:6
'''