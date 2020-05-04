name = "Michael Jackson"

#positive indexing
print(name[0])
print(name[6])
print(name[13])
print("\n")

#negative indexing
print(name[-1])
print(name[-15])
print(len(name))
print("\n")

#slicing
print(name[0:4])
print(name[8:12])
print("\n")

#stride
print(name[::2])
print(name[0:5:2])
print("\n")

#concatenate strings
print(name + "is the best")
print(3 * name)
print("Michael Jackson \n is the best" )
print(" Michael Jackson \t is the best")
print(r" Michael Jackson \ is the best")
print("\n")

#string operations
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)
print("\n")

A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
print(B)
print("\n")

print(name.find('el'))
print(name.find('Jack'))
print("\n")

#will print negative 1 if this cannot be found
print(name.find('Jasdfasdasdf'))

#Quiz on Strings
A = "1" #the ansewr is 1
B = "2" # the answer is 2
C = A + B # the answer is "12" not 3
print('\n')

D = "ABCDEFG"
print(D[:3])
print("\n")

E = 'clocrkr1e1c1t'
print(E[::2])
print('\n')

print("\\")
print('\n')

F = "You are wrong"
print(F.upper())
print('\n')

G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(G.find("snow"))

print(G.replace("Mary" , "Bob"))
