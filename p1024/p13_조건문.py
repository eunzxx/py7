#조건문은 else가 없으면 if에서 false이면 아무일도 일어나지 않음.
#if절이 true일 경우는 else 생략해도 출력 가능

if 10>5:     
    print("정상입니다.")
    
# if문 꼭 :으로 닫아줘야 함.
# 아래 문구는 무조건 들여쓰기를 해줘야 함. 
# if(10>5):
#    print("정상입니다.")
# else: 
#   print("비정상입니다.") 


 
# 숫자를 입력받아 100보다 큰 수인지 아닌지 출력하시오.
# 100보다 큰 수입니다. 100보다 작은 수입니다.

num = int(input("숫자를 입력하세요."))
if(num>100):
    print("100보다 큰 수입니다.")
else: 
   print("100보다 작은 수입니다.") 
   


   
# 입력된 숫자가 짝수인지 홀수인지 출력하시오.
# 짝수입니다. 홀수입니다.
# num%2 == 0
#num=int(input("숫자를 입력하세요."))
#if((num%2)==1):
#    print("홀수입니다.")
#else:
#    print("짝수입니다.")

# 내부모듈 (=내장모듈, 파이썬에서 제공해주는 모듈. **외워두기**)
import datetime
now = datetime.datetime.now()
print(now)

print(now.year,"년도")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

#입력한 주민번호의 월을 파악해서 현재 날짜와 같은 월이면
#이벤트 대상입니다. or not 이벤트 대상이 아닙니다. 출력하시오.

jumin = input("주민번호를 입력하세요.")
today = datetime.datetime.now()
if(int(jumin[2:4])==(today.month)):
    print("이벤트 대상입니다.")
else:
    print("이벤트 대상이 아닙니다.")


str1 = "abcdefg"
# [시작번호:끝번호:스탭]
print(str1[1:6:2])  #bdf
print(str1[:5])     #abcde
print(str1[5:2:-1]) #fed
print(str1[::-1])   #gfedcba


# 포맷(**참고**)
#n = "03"
#print(int(n))
#n2 = 3
#print("%02d" % n2)