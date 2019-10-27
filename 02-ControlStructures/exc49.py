nr_dnia_Tygodnia = 4
days = ["PN", "WT", "SR", "CZ", "PT", "SB", "ND"]
day = 1
for i in days:
    print(f"| {i} |", end="")
print()
for i in range(0, 7):
    if i >= nr_dnia_Tygodnia:
        print(f"|  {day} |", end="")
        day += 1
    else:
        print("|    |", end="")
print()
for i in range(day, 36-nr_dnia_Tygodnia):
    if 31 > i >= 10:
        print(f"| {i} |", end="")
    elif i < 10:
        print(f"|  {i} |", end="")
    elif i >= 31:
        print("|    |", end="")
    if (i + nr_dnia_Tygodnia) % 7 == 0:
        print()
