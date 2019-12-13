class Song:
    def __init__(self, singer, title, album, year):
        self.singer = singer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        str1 = "{0:<10} {1}\n".format("Wykonawca:", self.singer)
        str2 = "{0:<10} {1}\n".format("Tytuł: ", self.title)
        str3 = "{0:<10} {1}\n".format("Album: ", self.album)
        str4 = "{0:<10} {1}\n".format("Rok: ", self.year)
        return str1 + str2 + str3 + str4


nie_ma_fal = Song("Dawid Podsiadło", "Nie ma fal", "Małomiasteczkowy", 2018)
back_to_you = Song("Selena Gomez", "Back to you", "13 Reasons why", 2018)
najnowszy_klip = Song("Dawid Podsiadło", "Najnowszy klip", "Małomiasteczkowy", 2019)

print(nie_ma_fal)
print(back_to_you)
print(najnowszy_klip)
