class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Fortuner")
car2 = Car("Hyundai", "Creta")

car1.display_info()
print()
car2.display_info()

