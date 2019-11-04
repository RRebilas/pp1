import re


def vowels(text):
    vowelCount = re.findall('[aeiou]', text)
    return len(vowelCount)


text = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."

print(vowels(text))
