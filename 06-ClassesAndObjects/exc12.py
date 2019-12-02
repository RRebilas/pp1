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

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no


tv = TV()
tv.show_status()
tv.on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.off()
tv.show_status()