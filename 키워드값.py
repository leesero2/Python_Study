def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석",main_lang="파이썬",age=20) # 유재석 20 파이썬
profile(main_lang="자바",age=25,name="김태호") # 김태호 25 자바

# 함수에서 전달받은 매개변수는 값의 순서 상관없이 잘 전달이 됨.
