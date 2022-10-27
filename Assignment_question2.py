import random
Cons_No = int(input("Enter your consumer no.:"))
units = int(input("Enter the number of units consumed:"))
cost= None
Base_cost = 75
if units <= 100:
    cost = 2.50*units
elif units>100 and units<=200:
    cost = (2.50*100)+(3.50*(units-100))
elif units>200:
    cost = (2.50*100)+(3.50*100)+(5.00*(units-200))
print("\t\tBangalore Electricity Board")
print("Date:08-08-2020/t Bill No.:",random.randint(1,2000))
print("Consumer No.:",Cons_No)
print("__________________________________________________________________")
print("No. of units consumed     :",units)
print("Total Charge              :",Base_cost+cost)
print("__________________________________________________________________")
