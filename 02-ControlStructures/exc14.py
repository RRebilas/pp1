age = int(input("Podaj wiek psa w ludzkich latach: "))
dog_age: float = 0
if age <= 2:
    dog_age *= 10.5
else:
    dog_age *= 4
print("Wiek psa w psich latach to " + "{:.2f}".format(dog_age))
