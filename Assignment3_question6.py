s=input("Enter a sentence:")
word=input("Enter a word to search for:")
current_word=''
count=0
backwards=''
x=-1*len(s)
for i in s:
    if i ==' ':
        if current_word == word:
            count+=1
        for j in range(-1,(-1*len(current_word))-1,-1):
            backwards+=current_word[j]
        backwards+=' '
        current_word=''
    
    else:
        current_word+=i        

print("The word",word,"appears",count,"times in the sentence")
print(backwards)
