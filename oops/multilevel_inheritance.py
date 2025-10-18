class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand",self.brand)

class Phone(Device):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model

    def display_model(self):
        print("Model",self.model)


class SmartPhone(Phone):
    def __init__(self, brand,model,os):
        super().__init__(brand,model)
        self.os = os

    def display_os(self):
        print("Model", self.os)


s = SmartPhone("Samsung", "Galaxy S23", "Android")
s.display_brand()
s.display_model()
s.display_os()