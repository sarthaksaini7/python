first = 'John'
last = 'Smith'

full_name = first + ' [' + last + ']  is a coder'
print(full_name)


msg = f'{first} [{last}] is a coder'
print(msg)

year = input("what is you birth year? ")
age = 2020 - int(year)
greeting = f'{first} {last} is {age} years old'
print(greeting)
