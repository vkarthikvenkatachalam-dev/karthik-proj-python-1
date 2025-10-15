from itertools import count

phrase = input("enter a phrase: ")
vowels = ["a","e","i","o","u"]
seen=[]
for char in phrase:
    if char in vowels  and char not in seen:
        count = phrase.count(char)
        print(f"{char}={count}")
        seen.append(char)




