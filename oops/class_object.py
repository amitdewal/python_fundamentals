class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello, my name is ",self.name,"and i am",self.age)

person1 = Person("John",20)
person1.greet()

person2 = Person("Sara",19)
person2.greet()

