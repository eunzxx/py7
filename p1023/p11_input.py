### Quiz. num, num2 2개를 입력받아(-> '입력받아' 글자는 모두 인풋!) 숫자 타입으로 변경 후, 
# 사칙연산 결과를 출력하시오.
#input()  #-> 입력 가능, 출력 불가능
#print(input()) # -> 입력과 동시에 출력

num = int(input("숫자를 입력하세요.")) #문자열 타입 / 앞에 int를 넣으면 숫자타입
num2 = int(input("숫자를 입력하세요.")) #문자열 타입 / 앞에 int를 넣으면 숫자타입
print(num+num2)
print(num-num2)
print(num*num2)
print(num/num2)
