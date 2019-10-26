personal_number = input("Podaj nr PESEL: ")
age = 2018
gender = "mężczyzna" if int(personal_number[9]) % 2 != 0 else "kobieta"
# if personal_number[2] in range(1,2)
if 0 <= int(personal_number[2]) <= 1:
    year = "19" + personal_number[0:2]
    age -= int(year)
else:
    year = "20" + personal_number[0:2]
    age -= int(year)
print(f"Płeć: {gender}")
print(f"Wiek: {age}")