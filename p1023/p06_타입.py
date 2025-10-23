# 타입 - 숫자(정수-int, 실수-float), 문자열-str, 불 - bool(boolean : 참, 거짓)
# 타입이 굉장히 중요
print(100+100)
# print("100"+100) #문자열, 숫자는 덧셈 불가
num = "100"  #문자열
num2 = 100   #숫자-정수
num3 = 100.3 # 숫자-실수(소수점이 있는 숫자)
num4 = True  # boo1-참
num5 = False # bool-거짓
# num6 = true 에러 (소문자는 넣을 수 없음.)
num7 = "true" # 타입 - 문자열 (에러 아님.)
#자바는 문자열+숫자 가능, 파이썬만 문자열+숫자 불가능
# print(type(num7)) # type() 변수의 타입을 확인 가능, str -> string
num8 = None
print(num+num2) # 문자열, 숫자는 덧셈 불가