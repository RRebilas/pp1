num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))
num3 = int(input("Podaj trzecią liczbę: "))
array = [num1, num2, num3]
for i in array:
    if max(array) > i > min(array):
        print(i)
