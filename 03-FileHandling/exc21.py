num_array = []
lines_array = []
with open('numbersinrows.txt') as file:
    for line in file:
        lines_array.append(line.strip().split(","))
for line in lines_array:
    for num in line:
        num_array.append(int(num))
print(f"Ilość liczb naturalnych w pliku: {len(num_array)}")
print(f"Suma wszystkich liczb w pliku: {sum(num_array)}")