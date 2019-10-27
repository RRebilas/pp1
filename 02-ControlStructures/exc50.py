decimal_number = int(input("Podaj liczbe dziesietna: "))
binary = []
while decimal_number > 0:
    if decimal_number % 2 == 0:
        binary.append(0)
    else:
        binary.append(1)
    decimal_number = decimal_number // 2
binary.reverse()
for i in binary:
    print(i, end="")