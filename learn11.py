weight = input("Please enter your weight ")

unit = input("Please enter L for lbs & K for kilograms ")

if unit.upper() == "L":
    weight_kg = int(weight) * 0.45
    print(f'You are {weight_kg} kgs')
elif unit.upper() == "K":
    weight_lbs = int(weight) * 2.2
    print(f'You are {weight_lbs} lbs')
else:
    print("Please enter a valid unit of measurement")
