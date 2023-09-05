Iterating through a list and counting matching elements:

fruits = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana']
count = 0
target_fruit = 'apple'
for fruit in fruits:
    if fruit == target_fruit:
        count += 1
print(f'Found {count} occurrences of {target_fruit}.')
Iterating through a text string and counting specific letters:

text = 'Hello, world!'
target_letter = 'o'
count = 0
for letter in text:
    if letter == target_letter:
        count += 1
print(f'Found {count} occurrences of the letter {target_letter}.')
Iterating through a dictionary and printing keys and values:

student_scores = {'Alice': 95, 'Bob': 89, 'Charlie': 78, 'David': 92}
for name, score in student_scores.items():
    print(f'Student: {name}, Score: {score}')
Using enumerate to get indices and values from a list:

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'Index: {index}, Fruit: {fruit}')
