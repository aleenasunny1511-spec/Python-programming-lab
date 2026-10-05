s=input("Enter a sentence:")
print(s)
wordsList=s.split()
print(wordsList)
#use set to get unique words
uniqueWords=set(wordsList)
for words in uniqueWords:
    print(f"{words} occurs {wordsList.count(words)} times")
