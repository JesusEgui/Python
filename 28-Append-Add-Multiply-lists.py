Combining lists using append:

list_us = ['New York City', 'Chicago']
list_uk = ['London', 'Bristol']
list_all = []
list_all.extend(list_us)
list_all.extend(list_uk)
print(list_all)


Creating a list by repeating elements with append:

list_numbers = []
for _ in range(10):
    list_numbers.append(0)
    list_numbers.append(1)
print(list_numbers)


Creating a list of squares from 1 to 5 using append:

squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)
Creating a list of even numbers from 2 to 20 using append:


even_numbers = []
for x in range(2, 21, 2):
    even_numbers.append(x)
print(even_numbers)

Combining lists using the + operator:

list_us = ['New York City', 'Chicago']
list_uk = ['London', 'Bristol']
list_all = list_us + list_uk
print(list_all)


Creating a list by repeating elements:

list_numbers = [0, 1] * 10
print(list_numbers)


Creating a list of squares from 1 to 5 using list comprehension:

squares = [x ** 2 for x in range(1, 6)]
print(squares)


Creating a list of even numbers from 2 to 20 using list comprehension:

even_numbers = [x for x in range(2, 21, 2)]
print(even_numbers)
