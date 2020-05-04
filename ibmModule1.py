import sys
print(sys.version)

print("\n")
#check the type
print(type(11))
print(type(2.14))
print(type("Hello, Python 101!"))
print(type(12))
print("\n")
#check the type: int
print(type((-1)))
print(type(4))
print(type(0))
print("\n")
#check the type: float
print(type(1.0))
print(type(0.5))
print(sys.float_info)
print("\n")
#converting from one object type to a different object type
print(type(float(2)))
print(type(int(1.1)))
print(type(int('1')))
print(type(float('1.2')))
print("\n")
#converting numbers to strings
print(type(str(1)))
print(type(str(1.2)))
print("\n")
#boolean data type
print(type(True))
print(type(False))
print(type(int(True)))
print(type(bool(1)))
print(type(bool(0)))
print(type(float(True)))
print("\n")
#Exercises: Types
print("\n")
#What is the data type of the result of: 6/2
a = 6/2
print("The answer to this question would be: \n\t", (type(a)))
print("\n")
#The type of the result of: 6//2
b = 6//2
print("The answer to this qusetion would be: \n\t", type(b))
print("\n")
#Exercise: Expression and variables
#Let's write an expression that calculates how many hours there are in 160 minutes:
print("\n")
c = 160 / 60
print(c)
print("\n")
#Python follows well accepted mathematical conventions when evaluating mathematical expressions. In the following example, Python adds 30 to the result of the multiplication (i.e., 120
print(30 + 2 * 60)
print("\n")
#And just like mathematics, expressions enclosed in parentheses have priority. So the following multiplies 32 by 60.
print((30 + 2) * 60)
print("\n")
#Exercise
#What is the value of x where x = 3 + 2 * 2
x = 3 + 2 * 2
print(x)
print("\n")
#What is the value of y where y = (3 + 2) * 2?
y = (3 + 2) * 2
print(y)
print("\n")
#What is the value of z where z = x + y?
z = x + y
print(z)
print("\n")










