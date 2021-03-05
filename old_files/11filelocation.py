with open('myfile.txt',mode='r') as myfile: ## Opens file as a variable in READ ONLY MODE
    content=myfile.read() # Affix a variable to read the contents of the file

print(content) # Print the variable to display the contents of the file

with open('myfile.txt',mode='a') as myfile: # Opens the file as the same variable but now in APPEND ONLY MODE
    myfile.write('\nADDED NEW LINE')    # Write function to add/append a word to the end of the text file

with open('myfile.txt',mode='r') as myfile: # Opens the file again as the same variable but now in READ MODE
    newcontent=myfile.read() # Assign new variable to read and store the contents of the file
        
print(newcontent) # Display the new changed contents of the text file

with open('newfile.txt',mode='w') as newfile: # Write Mode overwrites any given file so create a new named file
    newfile.write('I created a new text file') # Add content inside the newly created file

with open('newfile.txt',mode='r') as newfile: # Open the new file as a new variable in READ MODE
    latest=newfile.read(); # Set variable to read the new file

print(latest) # Display the new file
