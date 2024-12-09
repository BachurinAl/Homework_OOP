from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avr_grade(self):
        if self.grades:
            grades_lst = []
            for g in self.grades.values():
                grades_lst.extend(g)
            return round(sum(grades_lst)/len(grades_lst), 1)
        return 0

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.avr_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.avr_grade() == student.avr_grade()
        return NotImplemented

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.avr_grade() < student.avr_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avr_grade(self):
        if self.grades:
            grades_lst = []
            for g in self.grades.values():
                grades_lst.extend(g)
            return round(sum(grades_lst)/len(grades_lst), 1)
        return 0

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avr_grade()}'

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avr_grade() == lecturer.avr_grade()
        return NotImplemented

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avr_grade() < lecturer.avr_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python разработчик']

lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached += ['Аналитик данных']

lecturer_3 = Lecturer('Semen', 'Zarev')
lecturer_3.courses_attached += ['Python разработчик']

rewiewer_1 = Reviewer('Alexander', 'Pronin')
rewiewer_1.courses_attached += ['Python разработчик']
rewiewer_1.courses_attached += ['Аналитик данных']

rewiewer_2 = Reviewer('Maksim', 'Nilolaev')
rewiewer_2.courses_attached += ['Python разработчик']
rewiewer_2.courses_attached += ['Аналитик данных']

student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progress += ['Python разработчик']
student_1.finished_courses += ['Введение в программирование на Python']

student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progress += ['Аналитик данных']
student_2.finished_courses += ['Аналитика и аналитическое мышление']

student_3 = Student('Nikita', 'Stepanov')
student_3.courses_in_progress += ['Python разработчик']
student_3.finished_courses += ['Введение в программирование на Python']

student_1.rate_hw(lecturer_1, 'Python разработчик', 7)
student_1.rate_hw(lecturer_1, 'Python разработчик', 8)
student_1.rate_hw(lecturer_1, 'Python разработчик', 9)

student_1.rate_hw(lecturer_2, 'Аналитик данных', 5)
student_1.rate_hw(lecturer_2, 'Аналитик данных', 7)
student_1.rate_hw(lecturer_2, 'Аналитик данных', 8)

student_2.rate_hw(lecturer_2, 'Аналитик данных', 10)
student_2.rate_hw(lecturer_2, 'Аналитик данных', 5)
student_2.rate_hw(lecturer_2, 'Аналитик данных', 6)

student_3.rate_hw(lecturer_3, 'Python разработчик', 5)
student_3.rate_hw(lecturer_3, 'Python разработчик', 6)
student_3.rate_hw(lecturer_3, 'Python разработчик', 7)

rewiewer_1.rate_hw(student_1, 'Python разработчик', 8)
rewiewer_1.rate_hw(student_1, 'Python разработчик', 9)
rewiewer_1.rate_hw(student_1, 'Python разработчик', 10)

rewiewer_2.rate_hw(student_2, 'Аналитик данных', 8)
rewiewer_2.rate_hw(student_2, 'Аналитик данных', 7)
rewiewer_2.rate_hw(student_2, 'Аналитик данных', 9)

rewiewer_2.rate_hw(student_3, 'Python разработчик', 8)
rewiewer_2.rate_hw(student_3, 'Python разработчик', 7)
rewiewer_2.rate_hw(student_3, 'Python разработчик', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print()

print(f'Перечень ревьюверов:\n\n{rewiewer_1}\n\n{rewiewer_2}')
print()
print()

print(f'Результат сравнения студентов по средней оценке за ДЗ: \n'
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')
print()
print()

print(f'Результат сравнения лекторов по средней оценке за лекции: \n'
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 < lecturer_2}')
print()
print()


def students_avr_hf(students, course):
    grades_lst = [student.grades for student in students if course in student.grades]

    sum_grades = []
    for grade in grades_lst:
        for g in grade.values():
            sum_grades += g

    return round(sum(sum_grades) / len(grades_lst), 1)


def lecturer_avr_hw(lecturers, course):
    grades_lst = [lecturer.grades for lecturer in lecturers if course in lecturer.grades]

    sum_grades = []
    for grade in grades_lst:
        for g in grade.values():
            sum_grades += g

    return round(sum(sum_grades) / len(grades_lst), 1)


res = students_avr_hf([student_1, student_2, student_3], 'Python разработчик')
print('Средняя оценка всех студентов:', res)

res = lecturer_avr_hw([lecturer_1, lecturer_2, lecturer_3], 'Python разработчик')
print('Средняя оценка всех лекторов:', res)