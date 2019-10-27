num = int(input("Podaj liczbę: "))
num2 = int(input("Podaj liczbę: "))
msg = f"Wynik: {num/num2}" if num2 != 0 else "Dzielenie przez 0!!"
print(msg)