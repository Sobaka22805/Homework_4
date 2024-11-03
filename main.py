class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'Person: {self.name} | {self.surname} | {self.age}')


class Group:
    def __init__(self, group_name: str, age_category: str):
        self.group_name = group_name
        self.age_category = age_category
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def info_group(self):
        print(f'Group: {self.group_name} | Age Category: {self.age_category} | Number of Students: {len(self.students)}')
        for student in self.students:
            student.info_student()


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, progress: float, group: Group):
        super().__init__(name, surname, age)
        self.progress = progress
        self.group = group
        self.group.add_student(self)  # Додаємо студента до групи
        self.pensione = self.set_pensione(self.age)

    def set_pensione(self, age: int):
        return age >= 60

    def info_student(self):
        print(f'Student: {self.name} | {self.surname} | {self.age} | Progress: {self.progress} | Pension: {self.pensione}')


class Worker(Person):
    def __init__(self, name: str, surname: str, age: int, position: str, duties: str):
        super().__init__(name, surname, age)
        self.position = position
        self.duties = duties
        self.pensione = self.set_pensione(self.age)

    def set_pensione(self, age: int):
        return age >= 60

    def info_worker(self):
        print(f'Worker: {self.name} | {self.surname} | {self.age} | Position: {self.position} | Duties: {self.duties} | Pension: {self.pensione}')


class Teacher(Person):
    def __init__(self, name: str, surname: str, age: int, subject: str, hours: int):
        super().__init__(name, surname, age)
        self.subject = subject
        self.hours = hours
        self.pensione = self.set_pensione(self.age)

    def set_pensione(self, age: int):
        return age >= 60

    def info_teacher(self):
        print(f'Teacher: {self.name} | {self.surname} | {self.age} | Subject: {self.subject} | Hours: {self.hours} | Pension: {self.pensione}')



group = Group(group_name="C2118", age_category="18-25")

student = Student(name="Діма", surname="Карайдала", age=18, progress=80.3, group=group)

worker = Worker(name="Богдан", surname="Александрович", age=35, position="Менеджер", duties="Керування командою")

teacher = Teacher(name="Константин", surname="Полишко", age=29, subject="Фізика", hours=15)

student.info_student()
worker.info_worker()
teacher.info_teacher()
group.info_group()
