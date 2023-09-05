
If-Elif-Else con múltiples condiciones:

user_age = int(input('What is your age? '))
if user_age < 18:
    print('You are under 18 years old')
elif 18 <= user_age < 30:
    print('You are between 18 and 29 years old')
else:
    print('You are 30 years old or older')
If anidado:
user_age = int(input('What is your age? '))
if user_age >= 18:
    if user_age < 30:
        print('You are between 18 and 29 years old')
    else:
        print('You are 30 years old or older')
else:
    print('You are under 18 years old')
Uso de operadores lógicos (and, or) en una condición:
is_student = input('Are you a student? (yes/no) ').lower()  # Convertimos la entrada a minúsculas
user_age = int(input('What is your age? '))
if user_age < 18 or is_student == 'yes':
    print('You qualify for a student discount')
else:
    print('You do not qualify for a student discount')
