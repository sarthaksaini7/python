def greeting():
    print('Hi there')
    print('Welcome aboard!')


print("Start")
greeting()
print("Finished")


def welcome_user(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("Welcome to the program")


def cost(base, tax, discount):
    totalcost = base+tax-discount
    print(f'The total cost of your order is {totalcost}')


welcome_user("Sarthak", "Saini")
welcome_user(last_name="Saini", first_name="Vijay")
cost(tax=50, base=10, discount=5)
