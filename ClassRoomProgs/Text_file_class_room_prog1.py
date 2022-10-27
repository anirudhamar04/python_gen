
def create_file():
    with open("text.txt","w") as f:
        n=int(input("Enter No. of lines:"))
        for i in range(n):
            str= input("Enter text:")
            f.write(str)
            f.write("\n")
        f.close()

def read_file():
    fname=input("Enter file name:")
    fname = fname + ".txt"
    f=open(fname,"r")
    str=f.read()
    print(str)
    f.close()

def copy_file():
    fname=input("Enter file name:")
    fname = fname + ".txt"
    f=open(fname,"r")
    f1 =open("Upcase.txt","w")
    str=" "
    while str:
        str=f.readline()
        for i in range(len(str)):
            if str[i].islower():
                str=str[:i]+str[i].upper()+str[i+1:]
        f1.write(str)
    f1.close()
    f.close()

def appnd_file():
    fname=input("Enter file name:")
    fname = fname + ".txt"
    with open(fname,"a") as f:
        m=int(input("Number of lines to be appended:"))
        for i in range(m):
            str=input("Enter string:")
            f.write(str)
            f.write('\n')
        f.close()
    
def count_digits():
    count=0
    fname=input("Enter file name:")
    fname = fname + ".txt"
    f=open(fname,"r")
    string=" "
    while string:
        string=f.readline()
        for i in string:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                count+=1
    f.close
    return count
                
        






while True:
    print("1.Create file")
    print("2.Display file")
    print("3.Copy File")
    print("4.Append File")
    print("5.Count digits")
    print("6.Quit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        create_file()
    elif choice == 2:
        read_file()
    elif choice == 3:
        copy_file()
    elif choice == 4:
        appnd_file()
    elif choice == 5:
        count=count_digits()
        print("No of digits",count)
    elif choice == 6:
        break
    else:
        print("Invalid input try again")

'''
1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:1
Enter No. of lines:3
Enter text:aaa 111
Enter text:bbb 222
Enter text:ccc 333
1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:2
Enter file name:text
aaa 111
bbb 222
ccc 333

1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:3
Enter file name:text
1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:2
Enter file name:Upcase
AAA 111
BBB 222
CCC 333

1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:4
Enter file name:text
Number of lines to be appended:3
Enter string:ddd 444
Enter string:eee 555
Enter string:fff 666
1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:5
Enter file name:text
No of digits 18
1.Create file
2.Display file
3.Copy File
4.Append File
5.Count digits
6.Quit
Enter your choice:6
'''