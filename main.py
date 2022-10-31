class Student:
    some_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.some_list.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Вы не можете оценивать этого лектора'

    def _averge_grade(self):
        sum_grades = 0
        len_grades = 0
        if self.grades == "":
            return '0'
        for grade in self.grades.values():
            sum_grades += sum(list(map(int, grade)))
            len_grades += len(grade)
        res = round(sum_grades / len_grades, 1)
        return res

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._averge_grade()}'
        res1 = f'\nКурсы в процессе изучения: {", ".join(str(course) for course in self.courses_in_progress)}\nЗавершенные курсы: {", ".join(str(course) for course in self.finished_courses)}'
        return res + res1

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} {other.surname} не является студентом!')
            return
        if self._averge_grade() > other._averge_grade():
            res = f'\n{self.name} {self.surname} лучше {other.name} {other.surname}'
        elif self._averge_grade() == other._averge_grade():
            res = '\nСтуденты на одном уровне'
        else:
            res = f'\n{other.name} {other.surname} лучше {self.name} {self.surname}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    some_list = []

    def __init__(self, name, surname):
        Lecturer.some_list.append(self)
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._averge_grade()}'
        return res

    def _averge_grade(self):
        sum_grades = 0
        len_grades = 0
        if self.grades == "":
            return '0'
        for grade in self.grades.values():
            sum_grades += sum(list(map(int, grade)))
            len_grades += len(grade)
        res = round(sum_grades / len_grades, 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} {other.surname} не является лектором!')
            return
        if self._averge_grade() > other._averge_grade():
            res = f'\n{self.name} {self.surname} лучше {other.name} {other.surname}'
        elif self._averge_grade() == other._averge_grade():
            res = '\nЛекторы на одном уровне'
        else:
            res = f'\n{other.name} {other.surname} лучше {self.name} {self.surname}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = grade
        else:
            return 'Вы не спец в данной области'

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}'
        return res

def  rating(some_list, course):
    sum_grades = 0
    len_grades = 0
    for object_class in some_list:
        if course in object_class.grades.keys():
            sum_grades += sum(list(map(int, object_class.grades[course])))
            len_grades += len(list(map(int, object_class.grades[course])))
    res = round(sum_grades / len_grades, 1)
    return res

student1 = Student('Ivan', 'Ivanov', 'man')
student2 = Student('Olga', 'Olegova', 'girl')
reviewer1 = Reviewer('Vasiliy', 'Vasilev')
reviewer2 = Reviewer('Kristina', 'Kristinova')
lecturer1 = Lecturer('Petr', 'Petrovsky')
lecturer2 = Lecturer('Gennady', 'Gennadyev')

student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['OOP']

student2.courses_in_progress += ['Python', 'OOP']
student2.finished_courses += ['Git']


reviewer1.courses_attached += ['Python']
reviewer1.rate_hw(student1, 'Python', [1, 2, 3, 4])
reviewer1.rate_hw(student2, 'Python', [2])

reviewer2.courses_attached += ['OOP']
reviewer2.rate_hw(student1, 'OOP', [5, 5])
reviewer2.rate_hw(student2, 'OOP', [2, 3])

lecturer1.courses_attached += ['Git']
lecturer2.courses_attached += ['Python', 'OOP']

student1.rate_lecture(lecturer1, 'Git', 10)
student1.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer1, 'Git', 9)
student2.rate_lecture(lecturer2, 'OOP', 2)
student2.rate_lecture(lecturer2, 'Python', 8)


print(student1)
print(lecturer1)
print(reviewer1)
print(lecturer1 > lecturer2)
print(student1 > student2)
print(rating(Student.some_list, 'OOP'))