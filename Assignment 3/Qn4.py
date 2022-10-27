import pickle
def create_file():
    f=open("accnt.dat","wb")
    n=int(input("Enter the number of entries:"))
    for i in range(n):
        acc_no=input("Enter Reg_no:")
        nm=input("Enter the Name:")
        balance=int(input("Enter the balance:"))
        temp={}
        TrType="NO Transaction"
        Transactionamt=0
        temp["Acc_no"]=acc_no
        temp["Name"]=nm
        temp["TransactionType"]=TrType
        temp["Transactionamt"]=Transactionamt
        temp["Balance"]=balance
        pickle.dump(temp,f)
    f.close()

def read():
    fname=input("Enter file name:")
    stu_file=open(fname+".dat","rb")
    temp={}
    print("Acc_No."+9*" "+"Name"+12*" "+"Transaction type"+"Transaction Amt "+"Balance")
    try:
        while True:
            temp=pickle.load(stu_file)
            for i in temp:
                print(str(temp[i])+(16-len(str(temp[i])))*" ",end="")
            print()
    except EOFError:
        print("Closing file...")
        stu_file.close()

def updt_bin():
    fname=input("Enter file name:")
    f=open(fname+".dat","rb")
    L=[]
    try:
        while True:
            temp=pickle.load(f)
            L.append(temp)
    except EOFError:
        print("End of File")
    acc_no= input("Enter the account number:")
    found=0
    for dic in L:
        if dic["Acc_no"]==acc_no:
            transaction= input("Enter transaction type:")
            transactionamt=int(input("Enter transaction amount:"))
            if transaction=="CREDIT":
                newbalance= dic["Balance"]+transactionamt
            elif transaction=="DEBIT":
                if (dic["Balance"]-transactionamt)>=1000:
                    newbalance= dic["Balance"]-transactionamt
                else:
                    print("Transaction not possible")
                    newbalance=dic["Balance"]
            dic["Balance"]=newbalance
            dic["TransactionType"]=transaction
            dic["Transactionamt"]=transactionamt
            found=1
    if found==1:
        f=open(fname+".dat","wb")
        for dic in L:
            pickle.dump(dic,f)
        f.close()
        print("Updation done")
    else:
        print("Record not Found")

while True:
    print("1. Create file:")
    print("2. Read file:")
    print("3. Update File:")
    print("4. Quit")
    choice=input("Enter your Choice:")
    if choice == "1":
        create_file()
    elif choice=="2":
        read()
    elif choice=="3":
        updt_bin()
    elif choice=="4":
        break
    else:
        print("Invalid input")

'''
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:1
Enter the number of entries:6
Enter Reg_no:SB_1234
Enter the Name:Sudhakar K
Enter the balance:10000
Enter Reg_no:SB_3425
Enter the Name:Malathi V
Enter the balance:12000 
Enter Reg_no:SB_5432
Enter the Name:Suhumar J ,   ssd xc
Enter the balance:12000
Enter Reg_no:SB_7654
Enter the Name:Vijay H
Enter the balance:15500
Enter Reg_no:SB_8765
Enter the Name:Suresh
Enter the balance:10500
Enter Reg_no:SB_7889
Enter the Name:Raghu 
Enter the balance:20000
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:2
Enter file name:accnt
Acc_No.         Name            Transaction typeTransaction Amt Balance
SB_1234         Sudhakar K      NO Transaction  0               10000
SB_3425         Malathi V       NO Transaction  0               12000
SB_5432         Suhumar J       NO Transaction  0               12000
SB_7654         Vijay H         NO Transaction  0               15500
SB_8765         Suresh          NO Transaction  0               10500
SB_7889         Raghu           NO Transaction  0               20000
Closing file...
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:3
Enter file name:accnt                                                                                                                               
End of File
Enter the account number:SB_1234
Enter transaction type:CREDIT
Enter transaction amount:5000
Updation done
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:2
Enter file name:accnt
Acc_No.         Name            Transaction typeTransaction Amt Balance
SB_1234         Sudhakar K      CREDIT          5000            15000
SB_3425         Malathi V       NO Transaction  0               12000
SB_5432         Suhumar J       NO Transaction  0               12000
SB_7654         Vijay H         NO Transaction  0               15500
SB_8765         Suresh          NO Transaction  0               10500
SB_7889         Raghu           NO Transaction  0               20000
Closing file...
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:3
Enter file name:accnt
End of File
Enter the account number:SB_3425
Enter transaction type:DEBIT
Enter transaction amount:600
Updation done
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:2
Enter file name:accnt
Acc_No.         Name            Transaction typeTransaction Amt Balance
SB_1234         Sudhakar K      CREDIT          5000            15000
SB_3425         Malathi V       DEBIT           600             11400
SB_5432         Suhumar J       NO Transaction  0               12000
SB_7654         Vijay H         NO Transaction  0               15500
SB_8765         Suresh          NO Transaction  0               10500
SB_7889         Raghu           NO Transaction  0               20000
Closing file...
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:3
Enter file name:accnt
End of File
Enter the account number:SB_8765
Enter transaction type:DEBIT
Enter transaction amount:10000
Transaction not possible
Updation done
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:2
Enter file name:accnt
Acc_No.         Name            Transaction typeTransaction Amt Balance
SB_1234         Sudhakar K      CREDIT          5000            15000
SB_3425         Malathi V       DEBIT           600             11400
SB_5432         Suhumar J       NO Transaction  0               12000
SB_7654         Vijay H         NO Transaction  0               15500
SB_8765         Suresh          DEBIT           10000           10500
SB_7889         Raghu           NO Transaction  0               20000
Closing file...
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:3
Enter file name:accnt
End of File
Enter the account number:SB_8237
Record not Found
1. Create file:
2. Read file:
3. Update File:
4. Quit
Enter your Choice:4
'''