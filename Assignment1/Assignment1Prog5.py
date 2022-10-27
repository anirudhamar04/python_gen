def Repeat(String,word):
    count=0
    prev=""
    for i in range(len(String)):
        
        if String[i]!=" ":
            prev+=String[i]
        else:
            if prev==word:
                count+=1
            prev=""
    return count

Sentence=input("Enter a string:")
Word=input("Enter word to be searched:")
Count=Repeat(Sentence,Word)
if Count==0:
    print("Word not found")
else:
    print("The word",Word,"appears",Count,"times in the sentence")

'''
Output
Enter a string:She sells sea shells on the sea floor
Enter word to be searched:sea
The word sea appears 2 times in the sentence
'''