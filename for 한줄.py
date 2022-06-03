# 출석번호가 1,2,3,4 앞에 100을 붙여서 101,102,103,104,...

students = [1,2,3,4,5]
print(students) # [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

# 학생 이름을 길이로 변환
student2 = ["Iron man","Thor","I am groot"]
student2 = [len(i) for i in student2] # student2의 데이터를 i에 하나씩 집어넣으면서 최종적으로 student2리 스트에 len(i)값을 대입
print(student2) # [8, 4, 10]

# 학생 이름을 대문자로 변환
student3 = ["Iron man","Thor","I am groot"]
student3 = [i.upper() for i in student3]
print(student3) # ['IRON MAN', 'THOR', 'I AM GROOT']