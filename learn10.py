name = input("Please enter your name ")

if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 50:
    print("Name must be less than 50 characters long")
else:
    print("Name looks good!")
