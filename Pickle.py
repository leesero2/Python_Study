# pickle 이란 프로그램에서 사용하는 데이터를 파일 형태로 저장해주는 기능

import pickle
# profile_file에 데이터를 작성(쓰기)
profile_file = open("profile.pickle","wb") # wb중 b는 바이너리, 피클파일은 인코딩 필요없음
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
pickle.dump(profile, profile_file) # profile  에 있는 정보를 profile_file에 저장
profile_file.close()
# profile_file이 생성됨

# profile_file에 데이터를 가져오려면(읽기)
profile_file = open("profile.pickle","rb") # 데이터를 불러오려면 "rb" 로 작성
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()
