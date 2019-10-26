for x in range(1, 11):
    row = ""
    if x <= 5:
        for y in range(x):
            row += "* "
    elif x > 5:
        for j in range(6, x-y, -1):
            row += "* "
    print(row)