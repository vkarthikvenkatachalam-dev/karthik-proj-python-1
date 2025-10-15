import string
data = input("enter password")
if len (data) < 8:
    print ("password is too short")
elif not any (char in string.ascii_uppercase for char in data):
    print("password is not having upper case letter")
elif not any(char in string.ascii_lowercase for char in data):
    print("password is not having lower case letter")
elif not any(char in string.digits for char in data):
    print("password is not having digits")
elif not any(char in string.punctuation for char in data):
    print("password is not having special characters")
elif " " in data:
    print("password doesnt include space")
else:
    print("password is valid")








