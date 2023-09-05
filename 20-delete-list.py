Removing a specific city from the list:

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
city_to_remove = 'Singapore'
if city_to_remove in top_cities:
    top_cities.remove(city_to_remove)
    print(top_cities)
else:
    print(f"{city_to_remove} is not in the list.")

Deleting multiple cities from a specific index to the end:

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
start_index = 3
end_index = len(top_cities)
if start_index < end_index:
    del top_cities[start_index:end_index]
    print(top_cities)
else:
    print('Invalid start and end indices.')
