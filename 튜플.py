# 튜플은 리스트와 비슷하나 데이터 변경이 안됨
# 그럼 튜플을 왜 사용하나, 속도가 리스트보다 빠름
# 튜플 구조
# 이름 = (내용,내용...)

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# menu.add("생선까스") - 에러 발생(튜플은 내용 변경 불가능)

# name = "이지훈"
# age = 25
# hobby = "코딩"
# print(name,age,hobby)

# 아래처럼 해도 됨
(name,age,hobby) = ("이지훈","25","코딩")
print(name,age,hobby) # 이지훈 25 코딩