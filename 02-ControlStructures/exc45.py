n = int(input("Ile liczb pierwszyść wyświetlić: "))
number = 2
num_count = 0
dividers_count = 0
msg = "Liczby pierwsze: "
while num_count < n:
    for i in range(2, number):
        if number % i == 0:
            dividers_count += 1
    if dividers_count > 0:
        dividers_count = 0
    else:
        msg += f"{number} "
        num_count += 1
    number += 1
print(msg)