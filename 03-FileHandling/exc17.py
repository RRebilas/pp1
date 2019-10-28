import re
string = 'To be, or not to be, that is the question'
vowel = re.findall('[aeiou]', string)
print(f"Liczba samoglosek: {len(vowel)}")