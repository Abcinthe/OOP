# example about OOP

class Student:

    def __int__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self, grade):
        self.grade = grade


class Course:

    def __int__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.name = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self, ):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s2 = Student("John", 18, 75)
s1 = Student('Tim', 18, 95)
s3 = Student('Bill', 18, 45)

course = Course('Math', 2)
course.add_student(s1)
course.add_student(s2)

print(course.add_student(s3))
print(course.students[0].name)