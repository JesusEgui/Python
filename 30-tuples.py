Creating a tuple with multiple data types:

mixed_tuple = (1, 'apple', True, 3.14)
print(mixed_tuple)


Nested tuples (tuples inside a tuple):

nested_tuple = (1, (2, 3), ('a', 'b', 'c'))
print(nested_tuple)


Tuple unpacking:

coordinates = (42.3601, -71.0589)
latitude, longitude = coordinates
print(f'Latitude: {latitude}, Longitude: {longitude}')


Using the zip function to create tuples from two lists:

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
name_score_tuples = list(zip(names, scores))
print(name_score_tuples)

empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3

user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)
