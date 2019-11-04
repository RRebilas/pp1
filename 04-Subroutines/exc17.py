import random


def rzucKostka():
    return random.randint(1, 6)


thrown = []
print("Wyrzucone oczka:", end=" ")
for i in range(3):
    thrown.append(rzucKostka())
    print(thrown[i], end=" ")
print(f"\nSuma oczek: {sum(thrown)}")
