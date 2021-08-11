import random

for i in range(3):
    number = random.randint(10, 20)
    print(number)

for i in range(5):
    members = ['John', 'Mary', 'Harry']
    leader = random.choice(members)
    print(leader)
