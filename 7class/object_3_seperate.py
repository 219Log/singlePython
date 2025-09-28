def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }


def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]


def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))


students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("윤명월", 64, 88, 92, 92),
    create_student("구지연", 88, 92, 98, 92),
    create_student("김연홍", 82, 86, 98, 88),
    create_student("이아람", 88, 74, 78, 92),
    create_student("이정후", 97, 92, 88, 95),
    create_student("정현화", 99, 82, 88, 86),
    create_student("김현곤", 88, 78, 78, 84),
    create_student("윤명월", 95, 85, 98, 98),
    create_student("이준서", 74, 72, 92, 90)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))