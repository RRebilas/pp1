class TV:
    def __init__(self):
        self.isOn = False
        self.channel_no = 1
        self.channels = []
        self.volume_level = 0

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

    def volume_up(self):
        if self.volume_level < 10:
            self.volume_level += 1

    def volume_down(self):
        if self.volume_level > 0:
            self.volume_level -= 1

    def show_volume_level(self):
        print(self.volume_level)


tv = TV()
tv.on()
tv.show_volume_level()
tv.volume_up()
tv.show_volume_level()
tv.volume_down()
tv.show_volume_level()
