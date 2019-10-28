num_arr = [32, 16, 5, 8, 24, 7]
with open('./numbersfromarray.txt', 'w') as file:
    for line in num_arr:
        file.write(f'{str(line)}\n')
