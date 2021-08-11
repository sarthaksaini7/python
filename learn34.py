# prime numbers in a range 100-200
for num in range(100, 200):
    if all(num % i != 0 for i in range(2, num)):
        print(num)

# fibonacci sequence


def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)


for i in range(0, 12):
    print(F(i))

list = [10, 20, 20, 30, 40, 50, 6, 100]

# reverse string


def rev(l):
    return (list[:: -1])


print(rev(list))

# star triangle


def pyfunc(r):
    for x in range(r):
        print(' ' * (r-x-1) + '*'*(2*x+1))


pyfunc(9)

# palindrome - reverse of  a sequence should be equal to original sequence
a = input("Enter the sequence: ")
b = a[::-1]
if a == b:
    print("palindrome")
else:
    print("Not a palindrome")
