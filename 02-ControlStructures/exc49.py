nr_dnia_Tygodnia = 6
days = ["PN", "WT", "SR", "CZ", "PT", "SB", "ND"]
day = 1
for i in days:
    print(f"| {i} |", end="")
print()
row = 5 if nr_dnia_Tygodnia + 30 > 35 else 4
for i in range(0, 7):
    if i >= nr_dnia_Tygodnia:
        print("|{0:^4}|".format(day), end="")
        day += 1
    else:
        print("|    |", end="")
print()
for i in range(row):
    for j in range(7):
        if day > 30:
            print("|    |", end="")
        else:
            print("|{0:^4}|".format(day), end="")
        day += 1
    print("")