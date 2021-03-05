print(4*(6+5))
print(4*6+5)
print(4+6*5)

question = 3+1.5+4
typeques = type(question)
print(typeques)

import math
number = 100
print(math.sqrt(number))

s= 'hello'
print(s[1])

s='hello'
print(s[::-1])

s='hello'
print(s[4])
print(s[-1])

list = [0,0,0]
print(list)
firstlist =[0,0]
secondlist = [0]
finallist = firstlist + secondlist
print(finallist)

list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
word = d['simple_key']
print(word)

d = {'k1':{'k2':'hello'}}
word2 = d['k1']['k2']
print(word2)

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
word3 = d['k1'][0]['nest_key'][1][0]
print(word3)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
word4 = d['k1'][2]['k2'][1]['tough'][2][0]
print(word4)

t=(1,2,3)
print(t)

list5=[1,2,3,54,23,34,2,2,5,4,3,3,3,3,4,5]
setlist = set(list5)
print(setlist)

