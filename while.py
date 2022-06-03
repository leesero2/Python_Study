# while은 어떤 조건이 만족할때까지 반복을 함
customer = "토르"
index = 5
person = "Unknown"
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
    index -=1
    if index == 0:
        print("커피는 폐기 되었습니다")
    # 토르, 커피가 준비 되었습니다. 5번 남았어요.
    # 토르, 커피가 준비 되었습니다. 4번 남았어요.
    # 토르, 커피가 준비 되었습니다. 3번 남았어요.
    # 토르, 커피가 준비 되었습니다. 2번 남았어요.
    # 토르, 커피가 준비 되었습니다. 1번 남았어요.
    # 커피는 폐기 되었습니다

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    # 동일 이름이 나왔을 경우 프로그램을 종료

