n=int(input("number if elements:"))
Mks=eval(input("The elements of the list Mks="))
highest=0
secondhighest=0
sumMks=0
aboveAvg=""
for i in Mks:
    if i>highest:
        secondhighest=highest
        highest=i
    sumMks+=i
avg=sumMks/n
for j in Mks:
    if j>avg:
        aboveAvg+=str(i)+','
print("Maximum Marks          :",highest)
print("Second maximum Marks   :",secondhighest)
print("Average Marks          :",avg)
print("Marks > Class average  :",aboveAvg)
