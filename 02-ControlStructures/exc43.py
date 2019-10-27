arr_num = []
msg = ""
for i in range(0, 3):
    arr_num.append(int(input("Podaj liczbę: ")))
arr_num.sort()
for i in arr_num:
    msg += f"{i}, "
print(f"Liczby w kolejności rosnącej {msg}")