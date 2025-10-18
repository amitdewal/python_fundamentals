# from oops.inheritance_exmaple import teacher1
# from oops.student_encapsulation import student1


class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print("Name: ",self.name)
        print("ID: ",self.id)

class Student(Person):
    def __init__(self, name, id,grade):
        super().__init__(name,id)
        self.grade = grade

    def display_grade(self):
        print("Grade: ",self.grade)

class Teacher(Person):
    def __init__(self, name, id,subject):
        super().__init__(name,id)
        self.subject = subject

    def display_subject(self):
        print("Subject: ",self.subject)



student1 = Student("John","101","10th")
teacher1 = Teacher("Mike","201","Science")

student1.display_info()
student1.display_grade()

print()
teacher1.display_info()
teacher1.display_subject()