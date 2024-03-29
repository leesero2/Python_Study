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

wraith1 = Unit("레이스",80,10)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 유닛 이름 : 레이스, 공격력 : 10

wraith2 = Unit("빼앗은 레이스",80,10)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 클로킹 상태입니다.".format(wraith2.name)) # 빼앗은 레이스 는 클로킹 상태입니다.