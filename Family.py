class Parent:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def speak(self):
        print('Welcome')


class Child(Parent):

    def speak(self):
        print('Thank you')


Child = Child('Tan', 14, 45, '130cm')
Child.speak()