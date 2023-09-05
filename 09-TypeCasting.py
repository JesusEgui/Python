Example 1: Age Calculation

# Age calculator: Calculate age in 10 years based on the birth year.

birth_year = int(input('What year were you born? '))
future_year = 2033  # Calculate age in the year 2033

age_in_2033 = future_year - birth_year
print('In', future_year, 'you will be', age_in_2033, 'years old, provided you live that long!')
Example 2: Temperature Conversion

# Temperature converter: Convert temperature from Celsius to Fahrenheit

temp_celsius = float(input('Enter the temperature today in Celsius degrees: '))
temp_fahrenheit = (temp_celsius * 9/5) + 32

temp_statement = str(temp_celsius) + ' degrees Celsius equal ' + str(temp_fahrenheit) + ' degrees Fahrenheit.'
print(temp_statement)
Example 3: Weight Conversion

# Weight converter: Convert weight from kilograms to pounds

weight_kg = float(input('Weight converter: Enter your weight in kilograms: '))
weight_lb = weight_kg * 2.20462  # 1 kilogram is approximately 2.20462 pounds

print('Your weight in pounds is:', weight_lb)
