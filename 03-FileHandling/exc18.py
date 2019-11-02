with open('numbers.txt') as file:
    num_array = [int(i) for i in file]
num_array.sort()
for num in num_array:
    print(num, end=" ")