# example about OOP

class Dog:
    def __init__(self, name, age):
        self.name = name
        # print(name)
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # def bark(self):
    #     print("bark")
    #
    # def add_one(self,x):
    #     return x + 1

d = Dog("Cat", 2)
print(d.name)
print(d.get_age())
d2 = Dog("Fish", 4)
print(d2.name)
print(d2.get_age())

# dogs_name = ['Cat', 'Fish']
# dogs_age = [32, 14]
# print(dogs_name)