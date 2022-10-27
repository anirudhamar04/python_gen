n=int(input("Enter number of products:"))
bill= dict()
gt=0
for i in range(n):
    p= input("Enter product name:")
    unit=int(input("Enter unit price:"))
    q= int(input("Enter Quantity:"))
    t= unit*q
    gt+=t
    elem=(unit,q,t)
    bill[p]=elem

gst=(0.15*gt)
final_gt = gt +gst

print(" "*15, "Sales done by class 6 E on Market Day")
print("_"*67)
print(" "*10,"Product"," "*23,"UP"," "*5,"Qty"," "*5,"Tot")

for j in bill:
    print(" "*10,j," " * (30-len(j)),bill[j][0]," " * (7-len(str(bill[j][0]))),bill[j][1]," " * (7-len(str(bill[j][1]))),bill[j][2])

print("_"*67)
print(" "*10,"Grand Total                                    :",gt)
print(" "*10,"GST                                            :",gst)
print(" "*10,"Net Price                                      :",final_gt)
print("_"*67)
