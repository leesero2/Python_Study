jihoon = "980226-1234567"

print("성별 : " + jihoon[7]) # 성별 : 1
print("연 : " + jihoon[0:2]) # 연 : 98
print("월 : " + jihoon[2:4]) # 월 : 02
print("일 : " + jihoon[4:6]) # 일 : 26

# 빈 공백은 0으로 간주
print("생년월일 : " + jihoon[:6]) # 생년월일 : 980226
print("주민번호 뒷자리 : " + jihoon[7:]) # 주민번호 뒷자리 : 1234567
print("주민번호 뒷자리 역출력 : " + jihoon[-7:]) # 주민번호 뒷자리 역출력 : 1234567