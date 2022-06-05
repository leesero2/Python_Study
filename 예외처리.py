# 예외처리란 예상치못한 프로그램의 에러가 발생시 후속조취를 취할 수 있게끔 하는 방법
# 문법 - try 에 원래 실행시킬 소스 넣고 except (에러문) 을 넣어야함. 다중 except 가능
try:
    print("나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError:
    print("0을 넣지마세요")
except:
    print("알 수 없는 에러 발생")
    # 무슨 에런지 보고싶다면 except Exception as err: 로 바꿔주면 끝

