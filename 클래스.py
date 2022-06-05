# 클래스는 와플 틀이라고 생각하면 됨 ( 틀을 만들면 계속 찍어낼 수 있음) 배럭(틀)하나에 마린(내용)이 계속 나오는것처럼

# 마린
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
#
# print("{0} 유닛이 생성되었습니다.".format(name)) # 마린 유닛이 생성되었습니다.
# print("체력 : {0}, 공격력 : {1}\n".format(hp,damage)) # 체력 : 40, 공격력 : 5
#
# # 탱크 : 포를 쏘고 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name)) # 탱크 유닛이 생성되었습니다.
# print("체력 : {0}, 공격력 : {1}\n".format(tank_hp,tank_damage)) # 체력 : 150, 공격력 : 35
#
# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))
#
# attack(name,"1시",damage) # 마린 : 1시 방향으로 적군을 공격 합니다. [공격력 5]
# attack(tank_name,"1시",tank_damage) # 탱크 : 1시 방향으로 적군을 공격 합니다. [공격력 35]

# 위처럼 하면 문제는 계속 유닛에 대한 상세 정보를 적어야함
# 아래처럼 클래스를 생성하면 코드 줄이 엄청 줄어듦

class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린",40,5)
marine3 = Unit("마린",40,5)
tank = Unit("탱크", 150, 35)

# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성 되었습니다.
# 체력 150, 공격력 35
