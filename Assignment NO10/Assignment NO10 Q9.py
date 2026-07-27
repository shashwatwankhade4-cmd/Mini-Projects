class Person:
    def __init__(self, name, age):
        # Added self parameter
        self.name = name
        self.age = age

    def introduce(self):
        # Added self parameter
        # Corrected print statement
        print("My name is", self.name, "and I am", self.age, "years old.")


p1 = Person("Rahul", 25)
p1.introduce()