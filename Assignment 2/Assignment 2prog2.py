def str_rev(s,n):
    global rev
    if n!=0:
        rev+=s[n]
        str_rev(s,n-1)
    else:
          rev+=s[0]
          print(rev)

L=[]
n=int(input("Enter number of elements:"))
for i in range (n):
    ele=input("Enter element:")
    L+=[ele]
print("Reverse of each element:")
for str1 in L:
    rev=" "
    n=len(str1)-1
    str_rev(str1,n)
    
'''
Enter number of elements:5
Enter element:anil
Enter element:rima
Enter element:amar
Enter element:uday
Enter element:nayan
Reverse of each element:
lina
amir
rama
yadu
nayan'''
