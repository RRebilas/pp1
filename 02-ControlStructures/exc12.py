x = int(input("x: "))
y = int(input("y: "))
msg = "x lub y jest liczbą ujemną" if (x < 0 or y < 0) else "Podane liczby są dodatnie"
print(msg)
