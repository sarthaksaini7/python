myfile = open('myfile.txt')
print(myfile.read())

## If file is read again then there will be no output as the cursor seek is at the end of the file and it will not print anything.
## In order to reread the file, the seek must be set back to 0.
print ("//BREAK")
myfile.seek(0)
content = myfile.read()
print(content)
print ("//BREAK")
myfile.seek(0)
content = myfile.readlines() ## each object is as a seperate item
print(content)

myfile.close()

