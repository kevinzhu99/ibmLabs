tuple1 = ("disco",10,1.2 )
print(tuple1)
print(type(tuple1))
print("\n")

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print("\n")

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print("\n")

# Use negative index to get the value of the last element
tuple1[-1]
print("\n")
# Use negative index to get the value of the second last element
tuple1[-2]
print("\n")

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
print("\n")

# Slice from index 0 to index 2
print(tuple2[0:3])
print("\n")
# Slice from index 3 to index 4
print(tuple2[3:5])
print("\n")
# Get the length of tuple
print(len(tuple2))
print("\n")

# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
# Sort the tuple

RatingsSorted = sorted(Ratings)
print(RatingsSorted)
print("\n")

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("\n")

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])
print("\n")

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])
print("\n")

# Print the first element in the second nested tuples
print(NestedT[2][1][0])
print("\n")

# Print the second element in the second nested tuples
NestedT[2][1][1]
print("\n")

# Print the first element in the second nested tuples
print(NestedT[4][1][0])
print("\n")

# Print the second element in the second nested tuples
print(NestedT[4][1][1])
print("\n")

#Quiz on Tuples
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")

print("The length of the tuple is: ", len(genres_tuple))
print("The element at the third index is:" , genres_tuple[3])
print("The objects from index is", genres_tuple[3:6])
print("The first two elements of the tuple is:", genres_tuple[:2])
print("The first index of disco is:", genres_tuple.index("disco"))
print('\n')

C_Tuple = (-5, 1, -3)
sortTuple = sorted(C_Tuple)
print(sortTuple)

