digits_array = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
number = (input("Podaj liczbe: "))
number_as_string = ""
for i in number:
    number_as_string += digits_array[int(i)] + " "
print(f"{number} - {number_as_string}")