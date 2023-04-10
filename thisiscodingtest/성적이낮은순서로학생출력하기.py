def solution(n, students):
    answer = []
    students.sort(key=lambda student:student[1])

    for student, _ in students:
        answer.append(student)

    return answer

n = 2
students=[('홍길동', 95), ('이순신', 77)]
print(solution(n,students))