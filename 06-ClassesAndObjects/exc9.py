class University:

    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'

    def print_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name

    def print_fullname(self):
        print(self.fullname)

    def set_fullname(self, new_name):
        self.fullname = new_name


uek = University()
uek.print_fullname()
uek.set_fullname('Akademia Górniczo Hutnicza w Krakowie')
uek.print_fullname()
