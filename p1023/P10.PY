# input() 함수
# input 함수는 문자열을 입력받는 함수, 입력받는 모든 것은 문자열 타입
# 문자열 + 숫자 : 불가능
# input1 = input("이름을 입력하세요.")
# input2 = input("나이를 입력하세요.") # 숫자를 입력받아도 문자열타입
# print(input1,input2)
# 주석처리 - 드래그한 후 Ctrl+'/'

# a = input("숫자를 입력하세요."), input은 모두 str타입, str타입 - 입력받는 모든 것 문자열타입
# print("100")
# print("100"+200) #문자열 + 숫자 -> 에러
# print(int(a)+200) #에러


### Quiz. num, num2 2개를 입력받아(-> '입력받아' 글자는 모두 인풋!) 숫자 타입으로 변경 후, 사칙연산 결과를 출력하시오.
num = input("숫자를 입력하세요.")
num2 = input("숫자를 입력하세요.")
print = (int(num)+int(num2))
print = (int(num)-int(num2))
print = (int(num)*int(num2))
print = (int(num)/int(num2))