import random


def random_number():
    return random.randint(1, 50)


random_array = []
even_count = 0
odd_count = 0
for i in range(1000):
    random_array += [random_number()]
    if random_array[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Liczby parzyste: {(even_count / len(random_array)) * 100}%")
print(f"Liczby nieparzyste: {(odd_count / len(random_array) * 100)}%")
