L=[8,7,9,9]
highest=0
second_highest=0
for i in L:
    if i>highest:
        second_highest=highest
        highest=i

print(second_highest)
