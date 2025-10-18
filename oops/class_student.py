class Student:
    total_students = 0; # class variable
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

    def display_info(self):
        print("Name: ",self.name)
        print("Grade: ",self.grade)

# override str method
    def __str__(self):
        return f"Student {self.name} grade: {self.grade}"

# override eq method

    def __eq__(self, other):
        return self.name == other.name and self.grade == other.grade

s1 = Student("John", "A")
s2 = Student("John", "B")
s1.display_info()
s2.display_info()


print(s1)
print(s2)

s3 = Student("Doe", "C")
s4 = Student("Doe", "C")

print(s4==s3)

print("Total student created: ", Student.total_students)
