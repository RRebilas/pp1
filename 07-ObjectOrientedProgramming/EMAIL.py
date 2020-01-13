import exc9

class EMAIL(exc9.Message):
    def __init__(self, from_who, to_who, subject, message):
        super().__init__()
        self.from_who = from_who
        self.to_who = to_who
        self.subject = subject
        self.message = super().set_message(message)

    def send(self):
        line1 = 'Wysyłanie email...\n'
        line2 = "{0:<7} {1}\n".format("Od:", self.from_who)
        line3 = "{0:<7} {1}\n".format("Do:", self.to_who)
        line4 = "{0:<7} {1}\n".format("Temat:", self.subject)
        line5 = "{0:<7} {1}\n".format("Treść:", self.message)
        return line1 + line2 + line3 + line4 + line5

    def __str__(self):
        return self.send()


msg = EMAIL('nowak@onet.pl', 'kowalski@gmail.com', 'Spotkanie w czwartek', "Informuje, że nasze czwartkowe spotkanie zostało odwołane.")
print(msg)
