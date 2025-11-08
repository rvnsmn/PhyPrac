username = input("Enter your username: ")

if len(username) > 12:
    print("Your username cannot be longer than 12 characters")
elif not username.find(" ") == -1:
    print("Your username should not have any space")
elif not username.isalpha():
    print("Your username should not have any numbers")
else:
    print("Welcome {username}")
    
