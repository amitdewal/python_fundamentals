class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display(self):
        print("brand: ",self.brand)
        print("Year: ",self.year)

class Car(Vehicle):
    def __init__(self, brand, year,model):
        super().__init__(brand, year)
        self.model = model


    def display(self):
        print("brand: ",self.brand)
        print("year: ",self.year)
        print("model: ",self.model)



car1 = Car("BMW", 1999, model="Model 1")
car1.display()
