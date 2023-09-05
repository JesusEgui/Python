Iterating through a list of tuples and accessing nested lists:

cities = [('New York', 'USA', [8.4, 8.5, 8.6]), ('Tokyo', 'Japan', [9.2, 9.4, 9.5]), ('Paris', 'France', [2.2, 2.3, 2.4])]
for city in cities:
    print('Name:', city[0], ', Country:', city[1])
    for population in city[2]:
        print('Population:', population)


Appending to a nested list inside a tuple:

person_data = ('Alice', 'Canadian', 1990, [165.2, 62.5])
person_data[3].append(63.0)
print(person_data)
These examples demonstrate how to work with lists inside tuples and how to iterate through a list of tuples with nested data structures.
  

city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Alegeria', 3.9)
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Alegeria', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])
    
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.6)
print(user_data)
