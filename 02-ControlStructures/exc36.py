number = 1
condition = True
while condition:
    if number % 7 == 0:
        for i in range(2, 7):
            if number % i == 1:
                if i == 6:
                    print(number)
                    condition = False
                else:
                    continue
            else:
                number += 1
                break
    else:
        number += 1
