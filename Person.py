class Person:
    number_of_Person = 0

    def __int__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def nummber_of_people(cls):
        return cls.number_of_Person()

    @classmethod
    def add_person(cls):
        cls.number_of_Person += 1


p1 = Person('Tim')
# print(Person.number_of_Person)
p2 = Person("Bill")
# print(Person.number_of_Person)
print(Person.number_of_Person())
