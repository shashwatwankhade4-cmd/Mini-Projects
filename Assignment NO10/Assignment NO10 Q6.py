class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self, percent):
        self.battery_percentage += percent
        if self.battery_percentage > 100:
            self.battery_percentage = 100

    def use_phone(self, minutes):
        self.battery_percentage -= minutes // 10
        if self.battery_percentage < 0:
            self.battery_percentage = 0

    def show_status(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery_percentage, "%")


phone = MobilePhone("Samsung", "S24", 60)

phone.show_status()
phone.use_phone(30)
phone.show_status()
phone.charge(20)
phone.show_status()