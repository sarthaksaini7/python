numbers = [5, 6, 5, 5, 5, 7, 8, 9]
numbers.append(20)
print(numbers)
numbers.insert(4, 17)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(8))
print(8 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.append(10)
print((numbers2))
print(numbers)

numbers.clear()
print(numbers)
