roll_no=int(input("Enter your roll number:"))
name=input("Enter your name:")
CourseCode=input("Enter your course code:")
if CourseCode == "A" or CourseCode == "a":
    Staionary_fee = 1200
    Tuition_fee = 15000
    Lab_fee = 1000
elif CourseCode == "B" or CourseCode == "b":
    Staionary_fee = 1500
    Tuition_fee = 20000
    Lab_fee = 2500
else:
    print("Wrong Course code. Re-enter code")
print("___________________________________________________")
print("Date: 09-08-2020\tDELHI PUBLIC SCHOOL")
print("Roll no:",roll_no,"\tName:",name,"Course Code:",CourseCode)
print("___________________________________________________")
print("Particulars       :               Rs.P")
print("___________________________________________________")
print("Stationary fee    :",Staionary_fee)
print("Tuition fee       :",Tuition_fee)
print("Lab fee           :",Lab_fee)
print("___________________________________________________")
print("Total fee    :",Staionary_fee + Tuition_fee + Lab_fee)      
print("___________________________________________________")
