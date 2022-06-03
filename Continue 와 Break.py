absent = [2,5] # 2,5 번이 결석했다고 가정
no_book = [7] # 책을 안가져왔다고 가정

for student in range(1,11):
    if student in absent: #student 안에 absent 값이 들어가 있다면,
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        #break 여기서 반복문을 종료시킴
    print("{0}, 책을 읽어봐".format(student))
    # 1, 책을 읽어봐
    # 3, 책을 읽어봐
    # 4, 책을 읽어봐
    # 6, 책을 읽어봐
    # 오늘 수업 여기까지. 7은 교무실로 따라와
    # 8, 책을 읽어봐
    # 9, 책을 읽어봐
    # 10, 책을 읽어봐

    # 2번과 5번이 생략함 continue 해당 반복을 건너뜀

