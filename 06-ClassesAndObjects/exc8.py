class University():
    def __init__(self):
        self.name = 'UEK'

    def print_name(self):
        print(self.name)

    def set__name(self, new_name):
        self.name = new_name


agh = University()
agh.set__name("AGH")
agh.print_name()
