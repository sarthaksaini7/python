numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#    text = number * "x"
#    print(text)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

new_numbers = [1, 1, 1, 1, 5]

for l_count in new_numbers:
    output = ''
    for count in range(l_count):
        output += 'x'
    print(output)
