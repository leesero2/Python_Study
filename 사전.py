cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

# get()을 써서 값을 가져오는것도 가능
print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 에러 발생 (keyError : 5) 에러발생 시점부터 프로그램 종료

# print(cabinet.get(5)) # 에러발생 (None) 단 에러가 발생해도 다음 프로그램도 실행됨.

# get()이랑 []이랑 차이가 에러가 발생한 시점으로부터 프로그램을 종료 시키느냐 마느냐에 차이

# in 을 이용하여 해당 키값에 데이터가 있는지 판단하는 방법
# (ket  in  변수)
print(3 in cabinet) # True
print(5 in cabinet) # False

# key값이 정수형일 필요는 없음
cabinet2 = {"A-3" : "이지훈", "B-100" : "윤혜린"}
print(cabinet2["A-3"]) # 이지훈
print(cabinet2["B-100"]) # 윤혜린

# 데이터를 추가
print(cabinet2) # {'A-3': '이지훈', 'B-100': '윤혜린'}
cabinet2["C-20"] = "이다훈"
cabinet2["A-3"] = "하진성" # 해당 키에 이지훈 데이터가 있지만 변경이 가능
print(cabinet2) # {'A-3': '하진성', 'B-100': '윤혜린', 'C-20': '이다훈'}

# 데이터 삭제
del cabinet2["A-3"]
print(cabinet2) # {'B-100': '윤혜린', 'C-20': '이다훈'}

# key 들만 출력
print(cabinet2.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet2.values()) # dict_values(['윤혜린', '이다훈'])

# key, value 쌍으로 출려갛려면
print(cabinet2.items()) # dict_items([('B-100', '윤혜린'), ('C-20', '이다훈')])

# 모든 데이터를 지우는 방법
cabinet2.clear()
print(cabinet2) # {}