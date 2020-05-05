# Create a list
L = ["Michael Jackson", 10.1, 1982]
print('\n')
# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1])

# Sample List
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

# List slicing
L[3:5]

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print('\n')
print(L)

# Use append to add elements to list
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)
L.append(['a','b'])
print('\n')

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
print('\n')
# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
print('hard rock'.split())

print('\n')
# Split the string by comma
print('A,B,C,D'.split(','))

#Copy and Clone a list

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)
print('\n')

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])
print("A[0]:", A[0])

print('\n')

# Clone (clone by value) the list A
B = A[:]
print(B)
print('\n')
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])
print('A[0]:', A[0])

#Quiz on List
a_list = (1, "hello", [1,2,3], True)

#find the value at index 1 of a_list
print(a_list[1])

#retrieve the elements at index 1,2 and 3 of a_list
print(a_list[1:4])

#Concatenate the following A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a']
B = [2,1,'d']
C = A + B
print(C)
