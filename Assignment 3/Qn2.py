def create_file():
    with open("letter.txt","w") as f:
        n=int(input("Enter No. of lines:"))
        for i in range(n):
            str= input("Enter text:")
            f.write(str)
            f.write('\n')          

        f.close()

def read_file(fname):
    fname = fname + ".txt"
    f=open(fname,"r")
    str=" "
    while str:
        str=f.readline()
        for i in range(len(str)):
            if str[i].islower():
                str=str[:i]+str[i].upper()+str[i+1:]
            elif str[i].isupper():
                str=str[:i]+str[i].lower()+str[i+1:]
        print(str)
    f.close()

def word_search(fname,word):

    fname = fname + ".txt"
    f=open(fname,"r")
    str=" "
    while str:
        Count=0
        currenntWord=""
        str=f.readline()
        if str =="":
            break
        for i in str:
            if i == ' ':
                if currenntWord==word :
                    Count+=1
                currenntWord=""
            else:
                currenntWord+=i
        print("In the line:")
        print(str)
        print(word,"occurs",Count,"times in this line")
    f.close()
    

while True:
    print("1.Create file")
    print("2.Read File")
    print("3.Word Search")
    print("4.Quit")
    
    choice=int(input("Enter your choice:"))
    if choice == 1:
        create_file()
    elif choice == 2:
        fname=input("Enter file name:")
        read_file(fname)
    elif choice == 3:
        fname=input("Enter file name:")
        word=input("Enter word to be searched:")
        word_search(fname,word)
    elif choice == 4:
        break
    else:
        print("Invalid input try again")



'''
Output
1.Create file
2.Read File
3.Word Search
4.Quit
Enter your choice:1
Enter No. of lines:2
Enter text:1. C++ is an object oriented programming language
Enter text:2. Property of data abstraction 3. Concept of data hiding
1.Create file
2.Read File
3.Word Search
4.Quit
Enter your choice:2
Enter file name:letter
1. c++ IS AN OBJECT ORIENTED PROGRAMMING LANGUAGE

2. pROPERTY OF DATA ABSTRACTION 3. cONCEPT OF DATA HIDING


1.Create file
2.Read File
3.Word Search
4.Quit
Enter your choice:3
Enter file name:letter
Enter word to be searched:of
In the line:
1. C++ is an object oriented programming language

of occurs 0 times in this line
In the line:
2. Property of data abstraction 3. Concept of data hiding

of occurs 2 times in this line
1.Create file
2.Read File
3.Word Search
4.Quit
Enter your choice:4
'''