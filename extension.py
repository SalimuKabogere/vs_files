# Write a Python program that accepts a filename from the user 
# and prints the extension of the file.

# request for the user input of the file name
fileName=input("Enter the file name\n")
# split the filename 
fileExtension=fileName.split(".")
# prints the split user filename
print(fileExtension)
print("the file name is:\n")
# the file extensiopn is the last string hence at index -1
print(fileExtension[-1])
