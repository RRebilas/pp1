speed_limit = int(input("Podaj limit prędkości(km/h): "))
vehicle_speed = int(input("Podaj prędkość pojazdu: "))
substracted_speed = vehicle_speed - speed_limit
ticket = 0
if substracted_speed <= 0:
    print("Prawidłowa prędkość")
else:
    ticket = substracted_speed * 5 if substracted_speed <= 10 else (substracted_speed) * 15
print(f"Mandat (zł): {ticket}")
