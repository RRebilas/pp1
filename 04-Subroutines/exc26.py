def podatek(dochod):
    if dochod <= 5000:
        return dochod * 0.17
    else:
        return 5000 * 0.17 + (dochod - 5000) * 0.32


print(f"Podatek należny: {podatek(int(input('Podaj dochod: ')))}")
