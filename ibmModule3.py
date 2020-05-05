# If statement example

age = 19
#age = 18

# expression that can be true or false
if age > 18:
    # within an indent, we have the expression that is run if the condition is true
    print("you can enter")

# The statements after the if statement will run regardless if the condition is true or false
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")

print("move on")

# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")

print('do something..')

# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# Condition statement example

album_year = 1980

if (album_year > 1979) and (album_year < 1990):
    print("Album year was in between 1980 and 1989")

print("")
print("Do Stuff..")

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# Condition statement example

album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")

#Quiz on Conditions
print('Quiz Time')

rating = 8.5
if (rating > 8):
    print("This album is Amazing")
elif (rating <= 8):
    print("The album is ok")

album_year = 1979

if (album_year < 1980 or album_year == 1991 or album_year == 1993):
    print("This album came out already")

