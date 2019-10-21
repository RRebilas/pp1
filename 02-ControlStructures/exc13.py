x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
msg = ""
if x > 0 and y > 0:
    msg = "w pierwszej ćwiartce"
elif x < 0 and y > 0:
    msg = "w drugiej ćwiartce"
elif x < 0 and y < 0:
    msg = "w trzeciej ćwiartce"
elif x > 0 and y < 0:
    msg = "w czwartej ćwiartce"
elif x == 0:
    msg = "na osi y"
elif y == 0:
    msg = "na osi x"
else:
    msg = "na początku"
print(f"Punkt P({x}, {y}) znajduje się {msg} układu współrzędnych")
