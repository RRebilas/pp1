import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = b ** 2 - (4 * a * c)
if delta > 0:
    a1 = (-b - math.sqrt(delta)) / 2 * a
    a2 = (-b + math.sqrt(delta)) / 2 * a
    print(f"Pierwiastkami tego równania są liczby: {a1} oraz {a2}")
elif delta == 0:
    a0 = -b / (2 * a)
    print(f"Pierwiastkiem tego równania jest: {a0}")
else:
    print("Równanie nie posiada pierwiastków")
