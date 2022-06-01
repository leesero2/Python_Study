python = "Python is Amazing"

#lower() 함수는 전부 소문자로 변경시켜주는 함수
print(python.lower()) # python is amazing

#upper() 함수는 전부 대문자로 변경시켜주는 함수
print(python.upper()) #PYTHON IS AMAZING

#isupper() 함수는 해당 위치의 문자열이 대문자 인지 판별해주는 함수
print(python[0].isupper()) #True (python의 [0]번째 자리가 대문자여서 True 값 반환
print(python[1].isupper()) #False (python의 [1]번째 자리가 소문자여서 False 값 반환

#len() 함수는 해당 문자열의 길이를 출력시킴
print(len(python)) #17

#replace() 함수는 해당 지정 문자부분을 바꿔줌
#replace("원래 있던 내용" , "교체해줄 내용")
print(python.replace("Python", "Java")) #Java is Amazing

#index() 함수는 지정한 문자열의 위치를 알려줌
print(python.index("n")) #5 (n이 다섯번째 자리에 있기 때문)
# 단 이렇게 하면 처음에 n만 찾고 프로그램을 종료 시키기 때문에 뒤에 n은 알수 없음
#아래 처럼 하면됨

print(python.index("n",+ python.index("n") + 1)) #15 (두번째 위치의 n을 찾음)

#find() 함수는 index() 처럼 문자 위치를 알려줌 다만, 없는 문자열을 선언하면 -1을 출력함
print(python.find("n")) #5
print(python.find("java")) #-1
# print(python.index("java")) #에러발생

#count() 함수는 지정한 해당 문자열이 몇개 있는지 출력시켜줌
print(python.count("n")) # 2