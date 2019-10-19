# function to calculate
def celsius_convert(celsius_deg):
    fahrenheit = celsius_deg * 9 / 5 + 32
    kelvin = celsius_deg + 273.14
    print(f"{celsius_deg} stopni celsjusza to {fahrenheit} stopni fahrenheita oraz "
          f"{kelvin} stopni kelvina")


# input values
celsius_convert(int(input("Podaj stopnie celsjusza: ")))
