Finding the index of an element in a tuple:

user_data = ('John', 'American', 1964)
index = user_data.index('American')
print(f'The element "American" is at index {index} in the tuple.')


Counting the occurrences of an element in a tuple:

user_data = ('John', 'American', 1964, 'American', 'teacher')
count = user_data.count('American')
print(f'The element "American" appears {count} times in the tuple.')


Concatenating tuples to create a new tuple:

user_data = ('John', 'American', 1964)
additional_data = ('teacher', 'male')
combined_data = user_data + additional_data
print(combined_data)
