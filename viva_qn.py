numbers=list(range(0,51,4))
results=[]
for number in numbers:
    if not number%3:
        results.append(number)
print(results)
