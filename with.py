import pickle

# with는 close()를 할 필요가 없음
# 코드 자체가 매우 간결해짐


with open("profile.pickle","rb") as profile_file: # profile.pickle 파일을 연후 profile_file이라는 변수에 저장한 뒤
    print(pickle.load(profile_file)) # file 내용을 피클 로드를 통해 불러와서 출력
    # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

# 쓰기
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
    # 이러면 study_file 이라는 파일이 생기고 거기에 "파이썬을 열심히 공부하고 있어요" 라는 데이터가 저장됨

# 읽어오기
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read()) # 파이썬을 열심히 공부하고 있어요

