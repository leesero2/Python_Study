subway = [10,20,30]
print(subway) # [10, 20, 30]

subway = ["유재석","조세호","박명수"] # ['유재석', '조세호', '박명수']
print(subway)

# 조세호가 몇 번째 칸에 있는가?
print(subway.index("조세호")) # 1

#하하 씨가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈을 유재석과 조세호 사이에 넣어봄
# insert(넣을 인덱스위치,"삽입내용")
subway.insert(1,"정형돈")
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 뒤에서 부터 한명씩 제거
print(subway.pop()) # 하하 (삭제할 데이터)
print(subway) # ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop()) # 박명수
print(subway) # ['유재석', '정형돈', '조세호']

print(subway.pop()) # 조세호
print(subway) # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count("유재석")) # 2

# 정렬도 가능
num_list = [5,2,3,4,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
# num_list.clear()
# print(num_list) # []

# 다양한 자료형과 함께 사용 가능
mix_list = ["조세호",123,True]
print(mix_list) # ['조세호', 123, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list) # [5, 4, 3, 2, 1, '조세호', 123, True]