my_list = [1,2,3]
print(my_list)

my_list = ['STRING',1,2,3] ## lists can contain strings, numbers etc
print(my_list)

my_list = [1,2,3]
print(my_list[1:])

another_list = [7,8,9] 
new_list=my_list+another_list ## joining two different lists works
print(new_list)

new_list[0] = "ONE" ## can change items inside a list, by mentioning the index number
print(new_list)

new_list.append(10)  ##add item to end of the list
print(new_list)

new_list.pop() ##delete item from last index place of list
print(new_list)

popped_item = new_list.pop() ##delete item from last index and saves it in a variable
print(new_list)
print(popped_item)

popped_item = new_list.pop(0) ##delete item from first index
print(new_list)
print(popped_item)


new_list = ['a','x','e','d','c']
num_list = [1,2,3,4,5]

new_list.sort() ## sorts the list in an order
print(new_list)

numbers = [1,2,3,9,8,7,6]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

unsorted_list = [24,4634,623,656,213,4645,253346,723,52,7456,347345,24634,63,435,345,235245,235]
unsorted_list.sort()
print(unsorted_list)






