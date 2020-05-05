# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)
print('\n')

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)
print('\n')

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres
print('\n')

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)
print('\n')

# Add element to set
A.add("NSYNC")
print(A)
print('\n')

# Try to add duplicate element to the set
A.add("NSYNC")
print(A) #nothing happens to the set, cannot have duplicates
print('\n')

# Remove the element from set
A.remove("NSYNC")
print(A)
print('\n')

# Verify if the element is in the set
print("AC/DC" in A)
print('\n')

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set1)
print(album_set2)
print('\n')

# Find the intersections
intersection = album_set1 & album_set2
print(intersection)

# Find the difference in set1 but not set2
print(album_set1.difference(album_set2))
print(album_set2.difference(album_set1))

# Use intersection method to find the intersection of album_list1 and album_list2
print(album_set1.intersection(album_set2))

# Find the union of two sets
print(album_set1.union(album_set2))

# Check if superset
print(set(album_set1).issuperset(album_set2))

# Check if subset
print(set(album_set2).issubset(album_set1))

# Check if subset
print(set({"Back in Black", "AC/DC"}).issubset(album_set1))

# Check if superset
print(album_set1.issuperset({"Back in Black", "AC/DC"}))

print('\n')
#Quiz on Sets
list1 = ['rap','house','electronic music', 'rap']
setQuiz = set(list1)
print(setQuiz)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
aSum = sum(A)
bSum = sum(B)
#The answer is no
print(aSum)
print(bSum)

# Create a new set album_set3 that is the union of album_set1 and album_set2
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)

print(album_set1.issubset(album_set3))