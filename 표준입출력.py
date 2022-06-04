# sep는 문장 사이의 데이터를 삽입시킴
print("Python","Java", sep=",") # Python,Java
print("Python","Java", sep="vs") # PythonvsJava

print("Python","Java","JavaScript", sep="vs") # PythonvsJavavsJavaScript

# end는 문장을 줄바꿈없이 이어서 출력시킴
print("Python","Java", sep=",",end="?") # Python,Java?무엇이 더 재밌을가요?
print("무엇이 더 재밌을가요?")

import sys
# stdout는 표준 출력으로 문장이 찍힘
# stderr은 표준 에러로 처리가 됨
# 에러부분을 명시해서 수정할 수 있게끔 할때 사용
print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)

#시험성적
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items():  # 과목과 성적을 둘다 출력함 (for 'Key' 'value' in scores.items())
    print(subject.ljust(8),str(score).rjust(4), sep=":") # ljust는 왼쪽으로 8칸의 공간을 확보후 정렬 rjust는 오른쪽으로 4칸 공백후 정렬
    # 수학     :  0
    # 영어     : 50
    # 코딩     :100
    # 이렇게 출력이 됨

# 은행 대기순번표
# 001,002,003 ... 라고 붙게 하고싶다면
# zfill 함수를 사용하면됨.
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # 3개만큼의 공간을 확보후 값을 집어넣는데, 값을 지정하지 않을경우 0으로 채움
    # 대기번호 : 001
    # 대기번호 : 002
    #       .
    #       .
    # 대기번호 : 020

# 그냥 input은 정수형 값을 입력해도 모든 입력값을 문자열로 받아들임
# int(input()) 이런식으로 묶으면 정수형으로 인식함
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
