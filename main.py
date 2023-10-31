
#Створити ієрархію класів для опису академії.
# список класів: Person, Teacher, Student, Subject, Academy і т.д.
#Продумати архітектуру: реалізувати принципи ООП

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSex: {self.sex}")


class Teacher(Person):
    def __init__(self, name, age, sex, courtesy_title=None, position=None, subject=None):
        super().__init__(name, age, sex)
        self.courtesy_title = courtesy_title
        self.position = position
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Courtesy title: {self.courtesy_title}\nPosition: {self.position}\nSubject: {self.subject}")

Tetyana_Mykolaiyvna = Teacher("Tetyana Mykolaiyvna", 45, "female", "Mrs", "head teacher", "Ukrainian literature")
Tetyana_Mykolaiyvna.show_info()
class Student(Person):
    def __init__(self, name, age, sex, admission_year=None, group=None, average_point=None, curator=None):
        super().__init__(name, age, sex)
        self.admission_year = admission_year
        self.group = group
        self.average_point = average_point
        self.curator = curator

    def show_info(self):
        super().show_info()
        print(f"Admission year: {self.admission_year}\nGroup: {self.group}\nAverage point: {self.average_point}\nCurator: {self.curator}")

Serhii_Berezyn = Student("Serhii Berezyn", 10, "male", "2020", "3-A", 8.7, "Tetyana Mykolaiyvna")
Serhii_Berezyn.show_info()

class Academic_load:
    def __init__(self, course, hours_amount):
        self.course = course
        self.hours_amount = hours_amount

    def show_info(self):
        print(f"Course: {self.course}\nAmount of hours per year: {self.hours_amount}")

# Humanities = Academic_load("Third course", 720)
# Humanities.show_info()

class Subject(Academic_load):
    def __init__(self, course, hours_amount, subject_name, lecturer, room_number):
        super().__init__(course, hours_amount)
        self.subject_name = subject_name
        self.lecturer = lecturer
        self.room_number = room_number

    def show_info(self):
        print(f"Subject name: {self.subject_name}\nLecturer: {self.lecturer}\nRoom number: {self.room_number}")

Ukrainian_literature = Subject("Third course", 108, "Ukrainian literature", "Tetyana Mykolaiyvna", 207)
Ukrainian_literature.show_info()

