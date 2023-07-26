class Pet:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I an {self.name} and I am {self.age} year old")


class Cat(Pet):
    def __int__(self, name, age, color):
        super.__init__(name, age)
        self.color = color

    def speak(self):
        print("meow")

    def show(self):
        print(f"I an {self.name}, I am {self.age} year old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("bark")

class Fish(Pet):
    pass

p = Cat('blue', 45, "green")
p.show()
# p = Pet('Bill', 19)
# p.show()
# c = Cat('Tim', 88, "red")
# c.speak()
# d = Dog('john', 35)
# d.speak()
# f = Fish('Alan',18)