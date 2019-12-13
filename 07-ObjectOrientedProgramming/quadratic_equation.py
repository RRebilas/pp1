from math import sqrt as sqrt
coefficients = []
while True and len(coefficients) < 3:
    try:
        coefficients.append(float(input("Podaj współczynnik: ")))
    except ValueError:
        print("That wasn't a valid number. Try again!")
    else:
        print('Value confirmed')

a, b, c = coefficients

if a != 0:
    #calculate discriminant
    d = (b**2) - (4*a*c)
    if d < 0:
        print("Brak rozwiązań równania.")
    elif d == 0:
        x = -b / 2*a
        print(f"Pierwiastek równania to {x}")
    else:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print(f"Rozwiązania tego równania to {x1}, {x2}")
else:
    if b != 0:
        print("Brak rozwiązań równania")
    else:
        print("Wszystkie liczby są rozwiązaniem tego równania")