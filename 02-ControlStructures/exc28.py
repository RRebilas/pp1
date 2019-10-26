a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
for i in range(1, a + 1):
    side = ""
    for j in range(1, b + 1):
        if i in range(2, a):
            if j in range(2, b):
                side += " "
            else:
                side += "*"
        else:
            side += "*"
    print(side)