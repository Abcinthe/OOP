class Parent:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.member = []

    def speak(self):
        print('Welcome')

    def show_info(self):
        print(f'Name: {self.name} ,Age: {self.age} ,Weight: {self.weight} ,Height: {self.height}')


class Child(Parent):

    def speak(self):
        print('Thank you')


class GrandChild(Child):
    def __init__(self, name, age, weight, height, ID):
        super().__init__(name, age, weight, height)
        self.ID = ID

    def show_info(self):
        print(f'ID: {self.ID} ,Name: {self.name} ,Age: {self.age} ,Weight: {self.weight} ,Height: {self.height}')


Parent1 = Parent('Chien', 57, 75, '180cm')
Parent2 = Parent('Huong', 53, 49, '160cm')
Child1 = Child('Tan', 14, 45, '130cm')
Child2 = Child('Hoang', 25, 65, '175cm')

Parent1.speak()
Child1.speak()

GrandChild1 = GrandChild('Hoa', 18, 42, '170cm', 666999)
Parent1.show_info()
GrandChild1.show_info()
