class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

student1 = Student('김일',1234)
student1.add_grade('국어', 90)
student1.add_grade('영어', 80)
student1.add_grade('수학', 70)
print(f'학생이름 : {student1.name}')
print(f'평균성적 : {student1.get_average_grade()}')