x=str(input("enter a word:"))
vowels=0

for i in x:
    if("a"==i or "e"==i or "i"==i or "o"==i or "u"==i or "A"==i or "E"==i or "I"==i or "O"==i or "U"==i ):
        vowels+=1
print(vowels)
