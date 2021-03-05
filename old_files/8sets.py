## Sets are unodered collection of unique elements

myset = set() ## create a set by initializing a variable
print(myset)

myset.add(1)
print(myset)
myset.add(2) ## another 2 cannot be added to the set as all the elements must be unique inside the set
print(myset)

mylist = [1,1,1,1,2,2,2,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8] 
setlist = set(mylist) ## assign mylist unique elements into a set called "setlist"
print(setlist)