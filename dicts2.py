d={}
n=int(input("enter the no. of students:"))
for i in range(n):
    name=input("Enter the name:")
    Rollno=int(input("enter the roll no:"))
    marks=float(input("Enter marks:"))
    grade=input("Enter grade:")
    d[name]=[Rollno,marks,grade]
print(d)
