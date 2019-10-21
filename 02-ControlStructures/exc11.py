login = input("Podaj login: ")
password = input("Podaj haslo: ")
msg = "Podane dane są prawidłowe" if (login == "marek" and password == "m-123") else "Podane dane sa nieprawidłowe"
print(msg)
