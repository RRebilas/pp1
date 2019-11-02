import re

digits_sum = 0
with open("land.txt") as file:
    digits = re.findall(r"\d", file.read())
    for digit in digits:
        digits_sum += int(digit)
print(digits_sum)