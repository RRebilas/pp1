sum_even = 0
sum_odd = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Suma liczb parzystych: {sum_even}")
print(f"Suma liczb nieparzystych: {sum_odd}")
