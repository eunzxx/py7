# [산술연산자 (+(덧).-(뺄).*(곱),/(나),//(몫),%(나머지),**(제곱))]

#print(10+20)
#print(10-20)
#print(10*20)
#print(10/20)
#print(10/3)    #3.33333
#print(10//3)   #3
#print(10%3)    #1 (나머지)
#print(10**3)   #10*10*10 = 1000

# 두 수를 입력받아 위의 연산을 출력하세요.
num1 = int(input("숫자1을 입력하세요."))
num2 = int(input("숫자2을 입력하세요."))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print("%.2f" % (num1/num2))
print(num1//num2)
print(num1%num2)
print(num1**num2)

### 789원을 동전으로 교환,
### 500원, 100원, 50원, 10원짜리 동전 몇 개로 교환해야 할까요?
# 500 - 1개, 100 - 2개, 50 - 1개, 10 - 3개
# 값/500(몫), 나머지/100(몫), 나머지/50(몫), 나머지/10(몫) 
coin = 123456700
money1 = coin//500
money2 = coin%500
money3 = (money2//100)
money4 = (money2%100)
money5 = (money4//50)
money6 = (money4%50)
money7 = (money6//10)
print("500원 동전 : %d 개" % money1)
print("100원 동전 : %d 개" % money3)
print("50원 동전 : %d 개" % money5)
print("10원 동전 : %d 개" % money7)


coin = 1597000
# 50000원, 10000원, 5000원, 1000원 몇 장씩?
money1 = coin//50000
money2 = coin%50000
money3 = money2//10000
money4 = money2%10000
money5 = money4//5000
money6 = money4%5000
money7 = money6//1000

print("5만원 지폐 : %d 장" % money1)
print("1만원 지폐 : %d 장" % money3)
print("5천원 지폐 : %d 장" % money5)
print("1천원 지폐 : %d 장" % money7)

