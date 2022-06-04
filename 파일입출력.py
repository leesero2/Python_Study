
# 파일에 있는 내용 쓰기
score_file = open("score.txt","w",encoding="utf8") # "w"는 write쓰기
print("수학 : 0",file=score_file)
print("영어 : 0",file=score_file)
score_file.close() # 끝내면 꼭 닫아줘야함

# txt파일에 아래처럼 저장됨
# 수학 : 0
# 영어 : 0

score_file = open("score.txt","a",encoding="utf8") # 내용이 존재하는파일에 이어서 쓰려면 append를 의미하는 "a"를 적음
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
# write() 메소드는 따로 줄바꿈 기능이 없어서 \n입력해줘야함
# 아래처럼 생성됨
# 수학 : 0
# 영어 : 0
# 과학 : 80
# 코딩 : 100

# 파일에 있는 내용 읽어오기
score_file = open("score.txt","r", encoding="utf8") # "r" read를 의미
print(score_file.read())
score_file.close()
# 수학 : 0
# 영어 : 0
# 과학 : 80
# 코딩 : 100
# 위처럼 출력됨

# 다르게 읽어오기
score_file = open("score.txt","r", encoding="utf8")
# readline() 는 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# 줄바꿈을 하기싫으면 end=" " 를 뒤에 추가해주면 끝
print(score_file.readline()) # 수학 : 0
print(score_file.readline()) # 영어 : 0
print(score_file.readline()) # 과학 : 80
print(score_file.readline()) # 코딩 : 100
score_file.close()

# 위는 데이터가 몇줄인지 알고있지만 몇줄인지 모를때 출력하는 방법
score_file = open("score.txt","r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 만약 라인(데이터줄)이 없을경우
        break # 반복문 탈출
    print(line) # 줄바꿈 하기싫으면 역시나 end=" " 를 정의하면 됨
score_file.close()
# 아래처럼 출력됨
# 수학 : 0
#
# 영어 : 0
#
# 과학 : 80
#
# 코딩 : 100

# 리스트에 값을 넣은 후 처리하는 방법
score_file = open("score.txt","r", encoding="utf8")
lines = score_file.readline() # list 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()