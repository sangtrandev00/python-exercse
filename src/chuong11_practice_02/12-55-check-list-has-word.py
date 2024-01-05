str = input()
listWord = []
for word in str.split(' '):
    if(len(word) > 3):
        listWord.append(word)
print(listWord)
