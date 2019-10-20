array = [12, 6, 4, 9]
for i in range(len(array)):
    txt = ""
    for j in range(array[i]):
        txt += "*"
    print(f"{array[i]}: {txt}")
