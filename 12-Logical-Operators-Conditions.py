Comprobar si un número es par o impar:
python
Copy code
number = int(input('Enter a number: '))
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
Determinar si un año es bisiesto o no:
python
Copy code
year = int(input('Enter a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('The year is a leap year')
else:
    print('The year is not a leap year')
Clasificar un triángulo según sus lados:
python
Copy code
side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))

if side1 == side2 == side3:
    print('The triangle is equilateral')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('The triangle is isosceles')
else:
    print('The triangle is scalene')
