# Using the end argument to control line endings.
print('This is on', end=' ')
print('the same line.')
print('This is on', end='\n\n')
print('a new line.')
In this example, we use the end argument to control line endings, demonstrating how you can print multiple statements on the same line or add extra line breaks.

Example 2: Using sep Argument with Different Separators


# Using the sep argument with different separators.
fruits = ['apple', 'banana', 'cherry', 'date']

print('Fruits:', *fruits, sep=', ')
print('Colors:', 'red', 'green', 'blue', sep=' | ')
Here, we showcase the sep argument with different separators, such as a comma and a pipe (' | '), to format the output differently.

Example 3: Combining Multiple Keyword Arguments

# Combining multiple keyword arguments.
name = 'Alice'
age = 30

print('Name:', name, end=' | ')
print('Age:', age, sep=' - ')

# Custom separator using sep argument:
name = 'Alice'
age = 30
city = 'Wonderland'

print('Name:', name, 'Age:', age, 'City:', city)
print('Name:', name, 'Age:', age, 'City:', city, sep=' | ')

Example 1: Customizing the end Argument

# Customizing the end argument to change the line ending.
print('This is the end', end=' ')
print('of the line.')

Example 3: Customizing the sep Argument with Multiple Values

# Customizing the sep argument with multiple values.
fruits = ['apple', 'banana', 'cherry', 'date']

print('Fruits:', *fruits, sep=' | ')
