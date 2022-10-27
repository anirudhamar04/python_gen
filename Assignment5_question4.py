n=int(input("Enter number of students:"))
attendance= dict()
tot_abs=0
most_comp_key=""
most_comp_value=0
for i in range(n):
    name=input("Enter a name:")
    present=float(input("No of days present:"))
    absent=float(input("No of days absent:"))
    competition=float(input("No of days in a competition:"))
    tot_abs+=absent
    if present>118:
        present = 118
    if most_comp_value<competition:
        most_comp_key=name
        most_comp_value=competition
    elem = (present,absent,competition)
    attendance[name]=elem
absenteeism=tot_abs/n

print("Dictionary after Modification:")
print()
print("Name",6*" ","Present",3*" ","Absent",4*" ","Competition")
for j in attendance:
    print(j," " * (10-len(j)),attendance[j][0]," " * (10-len(str(attendance[j][0]))),attendance[j][1]," " * (10-len(str(attendance[j][1]))),attendance[j][2]," " * (10-len(str(attendance[j][2]))))
print()
print("Average absenteesim:",absenteeism)
print()
print("Students maximum days for competitions:",most_comp_key,most_comp_value,"days")

