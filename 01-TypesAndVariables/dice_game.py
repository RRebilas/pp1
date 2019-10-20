import random

computer_number = random.randint(1, 6)
user_number = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
print(f"Komputer wyrzucił: {computer_number}")
msg = 'True' if computer_number == user_number else 'False'
print(f"Zgadłeś: {msg}")
