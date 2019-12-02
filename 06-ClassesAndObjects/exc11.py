class TV:
    def __init__(self):
        self.isOn = False
        self.channel_no = 1

    def on(self):
        self.isOn = True

    def off(self):
        self.isOn = False

    def show_status(self):
        message = f"Telewizor jest załączony, {self.channel_no}" if self.isOn else "Telewizor jest wyłączony"
        print(message)


tv = TV()
tv.show_status()
tv.on()
tv.show_status()