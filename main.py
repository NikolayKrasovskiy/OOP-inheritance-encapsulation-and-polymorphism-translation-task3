class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finishedcourses = []
        self.coursesin_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_average_grade  # Уберите скобки
        courses_in_progress = ', '.join(self.coursesin_progress)
        finished_courses = ', '.join(self.finishedcourses)
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname} '
                f'Средняя оценка за домашние задания: {avg_grade:.1f} '
                f'Курсы в процессе изучения: {courses_in_progress} '
                f'Завершенные курсы: {finished_courses}')

    @property
    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0

    def __lt__(self, other):
        return self.get_average_grade < other.get_average_grade

    def __le__(self, other):
        return self.get_average_grade <= other.get_average_grade

    def __gt__(self, other):
        return self.get_average_grade > other.get_average_grade

    def __ge__(self, other):
        return self.get_average_grade >= other.get_average_grade

    def __eq__(self, other):
        return self.get_average_grade == other.get_average_grade

    def __ne__(self, other):
        return self.get_average_grade != other.get_average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_average_grade  # Уберите скобки
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname} '
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    @property
    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0

    def __lt__(self, other):
        return self.get_average_grade < other.get_average_grade

    def __le__(self, other):
        return self.get_average_grade <= other.get_average_grade

    def __gt__(self, other):
        return self.get_average_grade > other.get_average_grade

    def __ge__(self, other):
        return self.get_average_grade >= other.get_average_grade

    def __eq__(self, other):
        return self.get_average_grade == other.get_average_grade

    def __ne__(self, other):
        return self.get_average_grade != other.get_average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


def rate_lecturer(lecturer, course, grade):
    if course in lecturer.courses_attached:
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
    else:
        print(f'Cannot rate {lecturer.name} {lecturer.surname}, lecturer does not teach this course.')


def ratestudent(student, course, grade):
    if course in student.coursesin_progress:
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
    else:
        print(f'Review cannot be made, {student.name} is not enrolled in {course}.')


# Пример использования
best_student = Student('Ruoy', 'Eman', 'yourgender')
best_student.finishedcourses += ['Git']
best_student.coursesin_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades['Python'] = [8, 9, 10]

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']
ratestudent(best_student, 'Python', 9)

# Студент ставит оценку лектору
rate_lecturer(cool_lecturer, 'Python', 9)

# Вывод информации
print(cool_reviewer)
print(cool_lecturer)
print(best_student)

# Примеры сравнений
print(best_student > cool_lecturer)  # Сравнение студента и лектора
print(best_student < cool_lecturer)