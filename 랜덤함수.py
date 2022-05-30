from random import * #랜덤 함수를 사용하려면 라이브러리를 임포트 해야함

# 그냥 random() 함수를 사용하면 0.0 ~ 1.0 미만의 임의의 값(실수)을 생성함
print(random())

# 10을 곱하면 0.0 ~ 10.0 미만의 임의의 값(실수) 생성
print(random() * 10)

#정수값을 출력하고싶다면 int()로 묶으면 됨
print(int(random() * 10))

#1~10까지의 값을 출력하고싶다면
print(int(random() * 10)+1)

#1~45의 값을 출력하고싶다면
print(int(random() * 45) +1)

#좀더 간결하게 작성하려면
print(randrange(1,45)) # 1~45 '미만'의 임의의 값 생성

print(randint(1,45)) # 1~45 '이하'의 임의의 값 생성
