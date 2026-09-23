
class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"{self.name} {self.gpa}"

    def get_count(self):
        return f"Total # of student: {self.count}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.2)
student3 = Student("Sandy", 4.0)

print(student1.get_count())
