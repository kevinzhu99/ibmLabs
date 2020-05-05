# First function example: Add 1 to a and store as b
def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Get a help on add function
help(add)

# Call the function add()
add(1)
# Call the function add()
add(2)

# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)

# Use mult() multiply two integers
Mult(2, 3)
# Use mult() multiply two integers
Mult(2, 3)
# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")


# Function Definition
def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return (c)

# Initializes Global variable
x = 3
# Makes function call and return function a y
y = square(x)
print(y)

# Directly enter a number as parameter
square(2)


# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')

def MJ1():
    print('Michael Jackson')
    return (None)

MJ()
MJ1()
print('test')
print(MJ())
print(MJ1())

# Define the function for combining strings
def con(a, b):
    return(a + b)

# Test on the con() function
con("This ", "is")

#Functions make things simple
print('block1')
# a and b calculation block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5
c1

print('block2')
# a and b calculation block2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0
else:
    c2 = 5
c2

# Make a Function for the calculation above
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0
    else:
        c = 5
    return(c)

print('block3')
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1

print('block4')
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2

print('Using if/else statements and loops in functions')
# Function example
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])


# Example for setting param with default value
def isGoodRating(rating=4):
    if (rating < 7):
        print("this album sucks it's rating is", rating)

    else:
        print("this album is good its rating is", rating)

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)

# Example of global variable
myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

#Quiz on Functions
print('Quiz on Functions')

# Use the con function for the following question
def con(a, b):
    return(a + b)
#Answer: Yes, example con(2,5)

#Can the con function we defined before be used to concentrate a list or tuple?
#answer: Yes this is possible