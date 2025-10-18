class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
# __ means private
    #getter method
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks

    #setter method
    def set_marks(self, new_marks):
        if new_marks >=0:
            self.__marks = new_marks
        else:
            print("Invalid marks")


student1 = Student("John", 85)
print("Name:", student1.get_name())
print("marks:", student1.get_marks())

student1.set_marks(92)
# print("Name:", student1.get_name())
print("updated marks:", student1.get_marks())

student1.set_marks(-10) #Invalid marks