import random

dice_nums = ['Jedynka', 'Dwójka', 'Trójka', 'Czwórka', 'Piątka', 'Szóstka']
num_count = [0, 0, 0, 0, 0, 0]
for i in range(0, 100):
    num_count[random.randint(0, 5)] += 1
for i in range(0, 6):
    print(f"{dice_nums[i]}: {num_count[i]}")
