admn_no = input("Enter admission no.:")
class_ = input ("Enter your class:")
sec = input ("Enter your section:")
mark_E = int(input("enter your marks in English:"))
mark_M = int(input("enter your marks in Math:"))
mark_P = int(input("enter your marks in Physics:"))
mark_C = int(input("enter your marks in Chemisty:"))
mark_Comp = int(input("enter your marks in Computer science:"))
avg = (mark_E+mark_M+mark_P+mark_C+mark_Comp)/5
grade = None
if avg >=80:
    grade = 'A'
elif avg >=70 and avg < 80:
    grade = 'B'
elif avg >=50 and avg < 70:
    grade = 'C'
elif avg < 50:
    grade ='D'

print ("\t\t National Public School")
print ("\t\tRajajinagar. Banglore-10")
print ("Mark Sheet")
print("_________________________________________________________")
print("Admission Number         :",admn_no)
print("Class                    :",class_)
print("Sec                      :",sec)
print("Average                  :",avg)
print("Grade                    :",grade)
print("_________________________________________________________")
