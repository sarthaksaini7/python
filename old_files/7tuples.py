tuple = (1,2,3)
my_list = [1,2,3]
print(tuple)
print(my_list)

t = ('one',2)
print(t[0])

t_new = ('a','a','b')
print(t_new.count('a')) ## counts how many times 'a' occurs in the tuple

print(t_new.index('a')) ## displays the position when 'a' occurs first in the tuple
print(t_new.index('b'))

## Tuples do not support item assignment like lists do, as shown below

mylist= [1,2,3]
print("List = ", mylist)
mylist[0] = 'ONE'
print("Changed List = ", mylist)

