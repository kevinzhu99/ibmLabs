# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key
print(Dict["key1"])

# Access to the value by the key
print(Dict[(0, 1)])

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

# Get value by keys
print(release_year_dict['Thriller'])
print(release_year_dict['The Bodyguard'] )
print(release_year_dict.keys())
print(release_year_dict.values())
release_year_dict['Graduation'] = 2007
print(release_year_dict)
print('\n')
# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print('test\n')
print(release_year_dict)

print('quiz time')
#Quiz on Dictionaries
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic.keys())
print(soundtrack_dic.values())

album_sales_dict = {"Back in black" :50, "The Bodyguard" : 50, "Thriller" :65}
print(album_sales_dict["Thriller"])
print(album_sales_dict.keys())
print(album_sales_dict.values())