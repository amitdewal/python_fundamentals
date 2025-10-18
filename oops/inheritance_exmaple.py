# base class
class User:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id

    def display_info(self):
        print("Name: ",self.name)
        print("User id: ", self.user_id)


# student class
class Student(User):
    def __init__(self,name,user_id,grade):
        super().__init__(name,user_id)
        self.grade = grade

    def display_info(self):
        print("Name: ",self.name)
        print("User id: ",self.user_id)
        print("Grade: ",self.grade)




 #   teacher class
class Teacher(User):
     def __init__(self,name,user_id,subject):
         super().__init__(name,user_id)
         self.subject = subject

     def display_info(self):
         print("Name: ",self.name)
         print("User id: ",self.user_id)
         print("Subject: ",self.subject)



# admin class
class Admin(User):
    def __init__(self,name,user_id, permission):
        super().__init__(name,user_id)
        self.permission = permission

    def display_info(self):
        print("Name: ", self.name)
        print("User id: ", self.user_id)
        print("Permission: ", self.permission)


student1 = Student("Ravi","101","10th grade")
teacher1 = Teacher("Meena","201","Math")
admin1 = Admin("AdminUser","999","Full Access")

student1.display_info()
print()
teacher1.display_info()
print()
admin1.display_info()