for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))
    # 대기번호: 0
    # 대기번호: 1
    # 대기번호: 2
    # 대기번호: 3
    # 대기번호: 4

# range(범위) 를 해도 실행이 됨. 단 0부터 시작해서 입력한 번호 미만까지 실행이됨
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
    # 대기번호: 0
    # 대기번호: 1
    # 대기번호: 2
    # 대기번호: 3
    # 대기번호: 4

# range(1,6) 하면 1부터 6미만까지 실행이됨
for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))
    # 대기번호: 1
    # 대기번호: 2
    # 대기번호: 3
    # 대기번호: 4
    # 대기번호: 5

# 리스트 안의 값을 전부 출력하고싶다면
starbucks = ["아이언맨","토르","캡틴아메리카"]
for customer in starbucks:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    # 아이언맨, 커피가 준비 되었습니다.
    # 토르, 커피가 준비 되었습니다.
    # 캡틴아메리카, 커피가 준비 되었습니다.
