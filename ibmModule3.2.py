dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])

for i in range(0, 8):
    print(i)

for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

print('\n')

#while loops
dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while (year != 1973):
        year = dates[i]
        i = i + 1
        print(year)

print("It took ", i, "repetitions to get out of loop.")


#Quiz on Loops
print("Test time")

for i in range(-5,6):
    print(i)

print('pt2\n')
genresList = [ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in range(len(genresList)):
    print(genresList[i])

print('pt3\n')
squares=['red', 'yellow', 'green', 'purple', 'blue']

for i in range(len(squares)):
    print(squares[i])

print('pt4\n')
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
max = len(PlayListRatings)
while i != max:
    if PlayListRatings[i] > 6:
        print(PlayListRatings[i])
        i = i + 1
    else:
        print("invalid")
        break

print('pt5\n')
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

i = 0
max = len(squares)
while i != max:
    if (squares[i] == "orange") :
        new_squares.append(squares[i])
        i = i + 1
    else:
        break

print(new_squares)


