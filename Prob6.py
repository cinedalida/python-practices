#OOP

class Dog:

    #constructor to initialize object attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # function
    def bark(self):
        print(f"Woof! My name is {self.name}, I'm {self.age*7}, and I'm a {self.breed}")


# instance of a Dog class
my_dog = Dog("Oliver", 3, "Pomeranian")
# call bark
my_dog.bark()