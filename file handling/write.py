# First block - create and write to the file
with open("rahul.txt", "w") as file:  # Use "w" initially to create/overwrite
    file.write("i am a python developer.\n")  # Add newline

# Second block - append more content
with open("rahul.txt", "a") as file:
    file.write("i enjoy coding\n")
    file.write("i am improving at logic building\n")

# Third block - append lines from a list
lines = ["line1", "line2", "line3"]
with open("rahul.txt", "a") as file:
    file.writelines([line + "\n" for line in lines])

# Read and print the content
with open('rahul.txt', 'r') as file:
    content = file.read()
    print(content)


# t = 2
# print(dir(t))
