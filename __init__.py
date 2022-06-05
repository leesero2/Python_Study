# __init__ 이부분은 파이썬의 생성자임, 즉 객체가 생성될 때 자동으로 호출됨

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 아래처럼 하면 오류 발생 ( 함수에 정의된 매개변수만큼 똑같이 변수를 지정해야함)
# marine3 = Unit("마린")
# marine3 = Unit("마린",40)
