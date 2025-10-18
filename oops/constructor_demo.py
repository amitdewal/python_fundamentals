class Person:
    def __init__(self, name="Unknown", age=12):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


person1 =  Person("John", 18)
# person2 = person1()
person1.display_info()

person2 = Person("Doe", 11)
person2.display_info()

person2 = Person()
person2.display_info()
class Demo:
    pass
demo1 = Demo()
print(type(demo1))