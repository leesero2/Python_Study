gun = 10 # 전역변수 gun

def checkpoint(soldiers): # 경계근무하는 군인 수
    # gun = 20 # 지역변수 gun
    global gun # 변수앞에 global 을 붙이면 전역변수가 됨
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # [함수 내] 남은 총 : 8

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # [함수 내] 남은 총 : 6
    return gun

print("전체 총 : {0}".format(gun)) # 전체 총 : 10
checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun,2)
print("전체 총 : {0}".format(gun)) # 전체 총 : 6

