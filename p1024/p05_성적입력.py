# 이름 입력
# 국어 점수 입력
# 영어 점수 입력
# 수학 점수 입력
#합계
#평균
# % print 출력

name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
sum = int(kor+eng+math) # 더하기는 정수+정수+정수=정수
avg = sum/3  # 나누기를 하게되면 무조건 실수, f타입!

print(name)
print("%s" % name)  #나중에 국어점수/수학점수 등 입력하기 위한 폼
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,sum,avg))