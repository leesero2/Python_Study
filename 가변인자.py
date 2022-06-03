def profile(name,age,lang1,lang2,lang3,lang4,lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end=" " 줄바꿈을 하지 않는 다는 의미, 바로 이어서 출력함
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석",20,"Python","Java","C","C#","C++") # 이름 : 유재석	나이 : 20	 Python Java C C# C++
profile("김태호",25,"kotlin","Swift","","","") # 이름 : 김태호	나이 : 25	 kotlin Swift

# 사용할 수 있는 언어가 5개 이상일 경우
# 가변인자를 사용하면?
# 인자에 *를 붙여서 사용하면됨
def profile2(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end=" " 줄바꿈을 하지 않는 다는 의미, 바로 이어서 출력함
    for lang in language:
        print(lang,end = " ")
    print()

profile2("유재석",20,"Python","Java","C","C#","C++","JS") # 이름 : 유재석	나이 : 20	 Python Java C C# C++ JS
profile2("김태호",25,"kotlin","Swift","","","") # 이름 : 김태호	나이 : 25	 kotlin Swift



