names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[1])
print(names[2:])
names[0] = "Sarthak"
print(names)


numbers = [1, 29, 3, 4, 5, 6, 7, 8, 9, 10]

max = numbers[0]
for item in numbers:
    if item > max:
        max = item
print(max)
