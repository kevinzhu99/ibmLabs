# Download Example file
!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt

# Read the Example1.txt
example1 = "/resources/data/Example1.txt"
file1 = open(example1, "r")

# Print the path of file
print(file1.name)

# Print the mode of file, either 'r' or 'w'
print(file1.mode)

# Read the file
FileContent = file1.read()
print(FileContent)

# Type of file content
print(type(FileContent))

# Close file after finish
file1.close()

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed
print(file1.closed)

# See the content of file
print(FileContent)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

# Iterate through the lines
with open(example1, "r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1;

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
print(FileasList[0])
# Print the second line
print(FileasList[1])
# Print the third line
print(FileasList[2])