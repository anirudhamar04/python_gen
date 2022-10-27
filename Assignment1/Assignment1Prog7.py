def count_alpha(String):
    count=0
    for i in String:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            count+=1
    if count==0:
        print("No alphabets in the string")
    else:
        print("The number of alphabets:",count)

def count_symbols(String):
    count=0
    for i in String:
        if (ord(i)>=33 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=126):
            count+=1
    if count==0:
        print("No symbols in the string")
    else:
        print("The number of symbols:",count)

def rev_words(String):
    backwards=""
    words=String.split()
    for i in words:
        backwards+=i[::-1]
    return backwards    
Str=input("Enter String:")

while True:
    print("1.Count Alpha")
    print("2.Count symbols")
    print("3.Reverse Words")
    print("4.Quit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        count_alpha(Str)
    elif choice == 2:
        count_symbols(Str)
    elif choice ==3:
        rev=rev_words(Str)
        print(rev)
    elif choice == 4:
        break
    else:
        print("Invalid Input")


'''
Enter String:TC++ Compiler (version-4.5)
1.Count Alpha
2.Count symbols
3.Reverse Words
4.Quit
Enter your choice:1
The number of alphabets: 17
1.Count Alpha
2.Count symbols
3.Reverse Words
4.Quit
Enter your choice:2
The number of symbols: 6
1.Count Alpha
2.Count symbols
3.Reverse Words
4.Quit
Enter your choice:3
++CTrelipmoC)5.4-noisrev(
1.Count Alpha
2.Count symbols
3.Reverse Words
4.Quit
Enter your choice:3
'''