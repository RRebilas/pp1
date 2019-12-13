class Student:
    university = "UEK Kraków"
    number = 100000

    def __init__(self, name, surname, subject):
        self.name = name
        self.surname = surname
        self.album_no = Student.number
        self.subject = subject
        Student.number += 1

    def __str__(self):
        return f"{self.name} {self.surname} ({self.album_no}), {self.subject}, {Student.university}"


rafcio = Student('Rafał', 'Rębilas', 'Informatyka stosowana')
print(rafcio)
