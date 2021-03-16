numbers = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9, 10, 13, 14, 15, 16]

numbers.sort()
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
