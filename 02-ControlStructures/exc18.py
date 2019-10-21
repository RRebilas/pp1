msg = ""
for i in range(1, 31):
    if i % 3 == 0:
        msg = "THREE"
    elif i % 5 == 0:
        msg = "FIVE"
    else:
        msg = i
    print(msg)
