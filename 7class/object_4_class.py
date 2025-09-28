class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("윤명월", 64, 88, 92, 92),
    Student("구지연", 88, 92, 98, 92),
    Student("김연홍", 82, 86, 98, 88),
    Student("이아람", 88, 74, 78, 92),
    Student("이정후", 97, 92, 88, 95),
    Student("정현화", 99, 82, 88, 86),
    Student("김현곤", 88, 78, 78, 84),
    Student("윤명월", 95, 85, 98, 98),
    Student("이준서", 74, 72, 92, 90)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())