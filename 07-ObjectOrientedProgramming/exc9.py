class Message:
    def __init__(self):
        self.message = ''

    def set_message(self, message):
        self.message = message
        self.message = f"{self.message[:1].upper()}{self.message[1:].lower()} BYE."
        return self.message
