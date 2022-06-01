# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3} 중복을 허용하지 않기에 3은 하나만 출력됨

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집함 (자바와 파이썬을 모두 할 수 있는 개발자) 출력
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합(자바도 할 수 있거나 파이썬을 할 수 있는 개발자) 출력
print(java | python) # {'양세형', '김태호', '박명수', '유재석'}
print(java.union(python)) # {'양세형', '김태호', '박명수', '유재석'}

# 차집합 (자바는 할 수 있지만 파이썬은 못하는 개발자) 출력
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# 파이썬을 할 줄 아는 사람이 늘어났다면?
python.add("김태호")
print(python) # {'박명수', '유재석', '김태호'}

# java를 까먹었음
java.remove("김태호")
print(java) # {'유재석', '양세형'}

