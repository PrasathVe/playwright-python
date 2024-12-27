# Create a .txt file and place inside the location same in the file handling script folder [~READ FILE~]
f=open("color.txt", "r") # make the file and place inside the project folder
content = f.read()
print(content)
# Write File

# w=open("color.txt","r+")
# w.write("banana\n")
# w.write("Apple\n")
# w.write("Mango")
# w.close()

#r = read mode - We can read only
#w = write mode - we can write only
#r+ = we can read and write
#a = append we can write the data without losing the available data
#.read(), .write(), .readline() - print the first line