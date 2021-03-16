is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water today")

elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")

else:
    print("Its a lovely day")


print("Enjoy your day")

# question 1m house
is_goodcredit = False

price = 1000000
if is_goodcredit:
    downpayment = price * 0.1
    text = f'The downpayment for a good credit buyer is ${downpayment}'
    print(text)

else:
    downpayment = price * 0.2
    text = f'The downpayment for a bad credit buyer is ${downpayment}'
    print(text)
