previous = 0
next = 1
sum = 0

for i in range(0, 51):
    print(f"{previous} ")
    sum = previous + next
    previous = next
    next = sum