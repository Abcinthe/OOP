class Person:
    number_of_people = 0
    club = []

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def join_club(self, club):
        self.club = club


class Club():
    name = ''
    field = ''
    number_member = 0

    def __init__(self, name, field, number_member):
        self.name = name
        self.field = field
        self.number_member = number_member

    def show_club(self):
        print(self.name)
        print(self.field)
        print(self.number_member)


if __name__ == '__main__':
    person_1 = Person('Tim')
    print(Person.number_of_people)
    person_2 = Person("Bill")
    print(Person.number_of_people)
    print(Person.number_of_people_())
    #
    club_mu = Club('mu_fc', 'football', 100)
    person_1.join_club(club_mu)
    print(person_1.club.show_club())
