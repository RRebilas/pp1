num_array = []
with open('numbers.txt') as file:
    num_array = [int(i) for i in file]
with open('evennumbers.txt', 'w') as file:
    for i in num_array:
        if i % 2 == 0:
            file.write(f"{i}\n")
