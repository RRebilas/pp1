class TV:
    def __init__(self):
        self.isOn = False
        self.channel_no = 1
        self.channels = []

    def on(self):
        self.isOn = True

    def off(self):
        self.isOn = False

    def show_status(self):
        message = f"Telewizor jest załączony, {self.channel_no + 1} ({self.channels[self.channel_no]})" if self.isOn else "Telewizor jest wyłączony"
        print(message)

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        self.channels = channel_list

    def show_channels(self):
        print("LISTA KANAŁÓW TV")
        for i in range(len(self.channels)):
            print(f'{i+1} {self.channels[i]}')


tv = TV()
tv.on()
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Eleven Sports', 'TV4'])
tv.set_channel(3)
tv.show_status()
tv.show_channels()
tv.set_channel(5)
tv.show_status()