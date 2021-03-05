my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict['key1'])

prices = {'oranges':10, 'apple':20, 'milk':50}
print("Apple costs", prices['apple'])
print("Milk costs", prices['milk'])

d = {'k1':123, 'k2':[1,2,3,4,5], 'k3':{'InsideKey':100}}
print(d)
print(d['k1'])
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['InsideKey'])

x = {'key1':['a','b','c']}
print(x)
my_list = x['key1']
print(my_list)

print(x['key1'][2].upper())

new = {'k1':100, 'k2':200}
print(new)
new['k3'] = 300
print(new)
new['k1'] = "NEW VALUE INSERTED"
print(new)

print(new.keys())
print(new.values())
print(new.items())


