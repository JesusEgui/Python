Create a list of squares from 1 to 10:

squares = [x ** 2 for x in range(1, 11)]
print(squares)



Create a list of even numbers from 1 to 20:

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)



Create a list of strings containing the first letter of each day of the week:

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
initials = [day[0] for day in days_of_week]
print(initials)



numbers = [1, 2, 3, 4]
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(1, 101)]
print(numbers)

numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)
