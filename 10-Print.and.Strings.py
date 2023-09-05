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
