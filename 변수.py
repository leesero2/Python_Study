
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + " 이름은 " + name + "이에요")
print(name + "는 " + str(age)+"살 이며," +hobby+"을 아주 좋아해요") # 정수형을 print로 출력할때는 str()로 감싸줘야함
print(name + "는 어른일까요?"+ str(is_adult)) # 불리안을 print로 출력할때는 str()로 감싸줘야함
