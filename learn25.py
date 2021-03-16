try:
    age = int(input("Age: "))
    income = 2000000
    risk = income/age
    print(age)

except ZeroDivisionError:
    print("Age Cannot be Zero")

except ValueError:
    print("Invalid Value")
