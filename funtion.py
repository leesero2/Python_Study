# 함수는 정의만 해서는 실행이 안됨
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 이렇게 해당 함수를 호출해야 문장이 실행됨
open_account()

# 전달값과 반환값
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: #잔액이 출금금액보다 많으면
        print("{0}원이 출금되었습니다".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))

def withdraw_night(balance,money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 수수료 값과 전체 금액에서 출금과 수수료값을 뺀 값을 반환


balance = 0
balance = deposit(balance, 1000) # 인자로 money를 1000원 넣고 함수 호출후 리턴값을 balance에 저장
print(balance) # 리턴받을 값을 출력

# balance = withdraw(balance, 2000) # 출금이 완료되지 않았습니다. 잔액은 1000원 입니다.
# balance = withdraw(balance, 500) # 500원이 출금되었습니다

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은{1}원 입니다.".format(commission,balance))
