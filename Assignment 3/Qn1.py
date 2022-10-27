

def create_file():
    with open("letr.txt","w") as f:
        n=int(input("Enter No. of lines:"))
        for i in range(n):
            str= input("Enter text:")
            f.write(str)
            f.write("\n")
        f.close()

def read_file(fname):
    fname = fname + ".txt"
    f=open(fname,"r")
    str=" "
    while str:
        str=f.readline()
        print(str)
    f.close()

def read_file_vowel(fname):
    line=1
    fname = fname + ".txt"
    f=open(fname,"r")
    str=" "
    while str:
        Count=0
        str=f.readline()
        if str == "":
            break
        for i in str:
            if i in ['A','a','E','e','I','i','O','o','U','u']:
                Count+=1
        print("Number of vowels in line",line,":",Count)
        line+=1
    f.close()

def reverse_display(fname):
    fname = fname + ".txt"
    f=open(fname,"r")
    str=" "
    while str:
        str=f.readline()
        print(str[: :-1])
    
def copy_file(fname):

    fname = fname + ".txt"
    f=open(fname,"r")
    f1 =open("dup.txt","w")
    str=" "
    while str:
        currenntWord=""
        str=f.readline()
        for i in str:
            if i == ' ':
                if currenntWord[0] in ['A','a','E','e','I','i','O','o','U','u']:
                    f1.write(currenntWord)
                    f1.write(" ")
                currenntWord=""
            else:
                currenntWord+=i
        f1.write("\n")
    f1.close()
    f.close()


while True:
    print("1.Create file")
    print("2.Display file")
    print("3.Read file vowels")
    print("4.Reverse lines")
    print("5.Copy file")
    print("6.Quit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        create_file()
    elif choice == 2:
        fname=input("Enter file name:")
        read_file(fname)
    elif choice == 3:
        fname=input("Enter file name:")
        read_file_vowel(fname)
    elif choice == 4:
        fname=input("Enter file name:")
        reverse_display(fname)
    elif choice == 5:
        fname=input("Enter file name:")
        copy_file(fname)
    elif choice == 6:
        break
    else:
        print("Invalid input try again")





'''
1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:1
Enter No. of lines:3
Enter text:The get and getline are overloaded functions.
Enter text:The getline function extracts up to the delimiter.
Enter text:the get function can be used to extract character by character also.
1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:2
Enter file name:letr
The get and getline are overloaded functions.

The getline function extracts up to the delimiter.

the get function can be used to extract character by character also.


1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:3
Enter file name:letr
Number of vowels in line 1 : 16
Number of vowels in line 2 : 16
Number of vowels in line 3 : 20
Number of vowels in line 4 : 0
1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:4
Enter file name:letr

.snoitcnuf dedaolrevo era enilteg dna teg ehT

.retimiled eht ot pu stcartxe noitcnuf enilteg ehT

.osla retcarahc yb retcarahc tcartxe ot desu eb nac noitcnuf teg eht

1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:5
Enter file name:letr
1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:2
Enter file name:dup
and are overloaded 

extracts up

used extract




1.Create file
2.Display file
3.Read file vowels
4.Reverse lines
5.Copy file
6.Quit
Enter your choice:6
'''

