name = input("enter your name:").lower().replace("","")

i = 0
j = len(name)-1
is_palindrome = True
while i < j:
    if name[i] != name[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("word is palindrome")
else:
    print("word is not palindrome")













