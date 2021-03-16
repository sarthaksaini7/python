customer = {
    "Name": "Sarthak Saini",
    "Age": 30,
    "is_verified": True


}

print(customer.get("Age"))
print(customer.get("Birthday", "15th June"))

customer["Name"] = "John Smith"
print(customer["Name"])


words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
numbers = input("Numbers: ")
for number in numbers:
    output += words.get(number, "!") + " "

print(output)
