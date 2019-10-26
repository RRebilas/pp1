names_array = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']
longest_name = names_array[0]
for name in names_array:
    if len(name) > len(longest_name): longest_name = name
print(longest_name)
