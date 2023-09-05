Checking if a string contains only alphabetic characters:

input_text = input('Enter a word: ')
if input_text.isalpha():
    print('You entered a word with only alphabetic characters!')
else:
    print('Sorry, that\'s not a word composed only of alphabetic characters.')



Reversing a string:

original_string = 'Hello, world!'
reversed_string = original_string[::-1]
print(reversed_string)


Counting the occurrences of a character in a string:

text = 'Python programming is fun!'
char_to_count = 'a'
count = text.count(char_to_count)
print(f'The character \'{char_to_count}\' appears {count} times in the text.')



fav_band = 'Green Day'
print(fav_band[6])
print(fav_band[:6])

text = 'please capitalise me'
text_cap = text.upper()
print(text_cap)

user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')
