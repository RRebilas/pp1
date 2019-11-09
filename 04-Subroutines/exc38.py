import re


def upper_case(text):
    letters = re.findall("[A-Z]", text)
    string = ""
    for letter in letters:
        string += letter
    return string


print(upper_case("No Co Tam"))
