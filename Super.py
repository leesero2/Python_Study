# 상속 방법 : class 클래스 이름(상속할 클래스 이름)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(self.name,location,self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed,damage):
        Unit.__init__(self, name, hp, speed)  # Unit에서 매개변수를 상속받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 날 수 있는 공중 공격 클래스
class FlyalbeAttackUnit(AttackUnit, Flyable):  # 공격도 하면서 날줄 알아야 하기때문에 AttackUnit과 Flyable 클래스를 상속 받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 공즁유닛이라 지상속도는 0으로 설정
        Flyable.__init__(self, flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

# 건물
class buildingUnit(Unit):
    def __init__(self,name,hp,location):
        # Unit.__init__(self,name,hp,0) # 상속 받는 한가지 방법
        super().__init__(name,hp,0) # 이렇게 상속받아도 됨
        self.location = location
