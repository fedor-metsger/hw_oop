
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress) and \
            course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def avg_grade(self):
        s, cnt = 0, 0
        for c in self.grades:
            s += sum(self.grades[c])
            cnt += len(self.grades[c])

        if cnt: return round(s / cnt, 1)
        else: return None
      
    def __str__(self):
        fn_crss = ', '.join(self.finished_courses)
        crss_prg = ', '.join(self.courses_in_progress)
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" + \
            f"Средняя оценка за домашние задания: {self.avg_grade()}\n" + \
            f"Курсы в процессе изучения: {crss_prg}\n" + \
            f"Завершенные курсы: {fn_crss}"

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def avg_grade(self):
      s, cnt = 0, 0
      for c in self.grades:
          s += sum(self.grades[c])
          cnt += len(self.grades[c])

      if cnt: return round(s / cnt, 1)
      else: return None
      
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" + \
            f"Средняя оценка за лекции: {self.avg_grade()}"
            
    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
            course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avg_hw_grade(students, crs):
      s, cnt = 0, 0
      for stud in students:
          if crs in stud.grades:
              s += sum(stud.grades[crs])
              cnt += len(stud.grades[crs])
      if cnt: return round(s / cnt, 1)
      else: return None


def avg_lect_grade(lect, crs):
      s, cnt = 0, 0
      for l in lect:
          if crs in l.grades:
              s += sum(l.grades[crs])
              cnt += len(l.grades[crs])
      if cnt: return round(s / cnt, 1)
      else: return None

 
student_1 = Student('Андрей', 'Семёнов', 'м')
student_1.courses_in_progress += ['Python', 'Git']
student_2 = Student('Иван', 'Петров', 'м')
student_2.courses_in_progress += ['Python', 'Git']

mentor_1 = Reviewer('Аристарх', 'Кострицкий')
mentor_1.courses_attached += ['Python']
mentor_2 = Reviewer('Евстафий', 'Попундопуло')
mentor_2.courses_attached += ['Python']
mentor_3 = Lecturer('Тилапия', 'Штерн')
mentor_3.courses_attached += ['Python']
mentor_4 = Lecturer('Евпатий', 'Мормышкин')
mentor_4.courses_attached += ['Git']
mentor_5 = Lecturer('Доброслав', 'Жованович')
mentor_5.courses_attached += ['Python', 'Git']
 
mentor_1.rate_hw(student_1, 'Python', 9)
mentor_2.rate_hw(student_1, 'Python', 7)
mentor_1.rate_hw(student_2, 'Python', 6)

student_1.rate_lecturer(mentor_3, "Python", 8)
student_2.rate_lecturer(mentor_3, "Python", 9)
student_2.rate_lecturer(mentor_4, "Git", 7)
student_1.rate_lecturer(mentor_5, "Python", 10)
student_2.rate_lecturer(mentor_5, "Python", 9)
student_1.rate_lecturer(mentor_5, "Git", 8)
student_2.rate_lecturer(mentor_5, "Git", 9)


print("-------------------------\nstudent_1:\n", student_1, sep='')
print("-------------------------\nstudent_2:\n", student_2, sep='')
print("-------------------------\nmentor_1:\n", mentor_1, sep='')
print("-------------------------\nmentor_2:\n", mentor_2, sep='')
print("-------------------------\nmentor_3:\n", mentor_3, sep='')
print("-------------------------\nmentor_4:\n", mentor_4, sep='')
print("-------------------------\nmentor_5:\n", mentor_5, sep='')

print("-------------------------\nstudent_1 > student_2:", student_1 > student_2)
print("mentor_3 < mentor_4:", mentor_3 < mentor_4)

print("-------------------------\nСредняя оценка всех студентов по курсу Python:",
    avg_hw_grade([student_1, student_2], "Python"))
print("Средняя оценка всех студентов по курсу Git:",
    avg_hw_grade([student_1, student_2], "Git"))
print("Средняя оценка всех лекторов по курсу Python:",
    avg_lect_grade([mentor_3, mentor_4, mentor_5], "Python"))
print("Средняя оценка всех лекторов по курсу Git:",
    avg_lect_grade([mentor_3, mentor_4, mentor_5], "Git"))
