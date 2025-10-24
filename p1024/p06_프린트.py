# print("%d" % (100,200)) #에러, %자리와 뒤개수가 맞아야함
# print("%d %d" % 100)    #에러
print("%d %d" % (100,200))#%자리와 뒤개수가 일치

str1 = "이름"
str2 = "국어"
str3 = "영어"
str4 = "수학"
str5 = "합계"
str6 = "평균"
print(str1  ,str2  , str3  ,str4)                #띄어쓰기 안 됨
# \t 탭키적용: 띄어쓰기, \n : 줄바꿈
# 입력부분 
name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
sum = kor+eng+math
avg = sum/3

print("-"*50)
print("%s\t%s\t%s\t%s\t%s\t%s" % ("이름","국어","영어","수학","합계","평균"))  #4칸씩 띄어쓰기 가능
print("-"*50)
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,sum,avg))

