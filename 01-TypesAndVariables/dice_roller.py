import random

thrown_sum = 0
for i in range(3):
    number = random.randint(1, 6)
    print(f"Wylosowana liczba: {number}")
    thrown_sum += number
print(f"Suma wylosowanych liczb: {thrown_sum}")
