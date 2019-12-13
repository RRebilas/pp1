import exc9


class SMS(exc9.Message):
    def __init__(self, from_who, to_who, message):
        super().__init__()
        self.from_who = from_who
        self.to_who = to_who
        self.message = super().set_message(message)

    def send(self):
        line1 = 'Wysyłanie sms...\n'
        line2 = "{0:<7} {1}\n".format("Od:", self.from_who)
        line3 = "{0:<7} {1}\n".format("Do:", self.to_who)
        line4 = "{0:<7} {1}\n".format("Treść:", self.message)
        return line1 + line2 + line3 + line4

    def __str__(self):
        return self.send()


msg = SMS(512349223, 315234123, "Informuje, że nasze czwartkowe spotkanie zostało odwołane.")
print(msg)
