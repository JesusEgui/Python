dding a new entry to a dictionary:

contacts = {
    'John Smith': 'john.smith@email.com',
    'Jane Doe': 'jane.doe@email.com'
}
contacts['Alice Johnson'] = 'alice.johnson@email.com'
print(contacts)

------------------------------------------------------------------
Checking if a key exists in a dictionary before accessing it:

spanish_animals = {
   'dog': 'el perro',
   'cat': 'el gato',
   'horse': 'el caballo',
   'bird': 'el pájaro' 
}
animal = 'rabbit'
if animal in spanish_animals:
    print(f'The Spanish word for {animal} is {spanish_animals[animal]}')
else:
    print(f'Sorry, we don\'t have a translation for {animal}.')
  ------------------------------------------------------------------
Updating an existing entry in a dictionary:
python
Copy code
contacts = {
    'John Smith': 'john.smith@email.com',
    'Jane Doe': 'jane.doe@email.com'
}
contacts['John Smith'] = 'john.smith@newemail.com'
print(contacts)
