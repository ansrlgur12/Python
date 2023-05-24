print(39)             # 정수형 출력
print("문자열")
print([1,2,3,4,"5"])  # 리스트형
print(1+2)
print("파"+"이"+"썬")
print("파""이""썬")
print("파","이","썬")  # 콤마는 기본적으로 띄어쓰기가 포함되엉 있음
print("퍄\n\n\n이\n\n\n썬")
print("\"안녕하세요\"라고 말했습니다.")


# end와 sep옵션
print("Hello", end='@')
print("Python")

print(1,2,3,4,5,sep='\t')

print("010","5006","4146", sep="-")

year = 2023
month = 5
day = 24
print(year, month, day , sep="/")


# 다양한 출력 스타일
name = "곰돌이사육사"
age = 25
gender = "남성"
job = "소프트웨어 개발자"
addr = "경기도 고양시"

# C언어 스타일 : %로 서식을 지정하는 형식
print("="*5, "c 스타일", "="*5)
print("이름 : %s"%(name))
print("나이 : %s"%(age))
print("성별 : %s"%(gender))
print("직업 : %s"%(job))
print("주소 : %s"%(addr), end="\n\n")

# Python 스타일 (3.6 이전버전)
print("="*5, "python old style", "="*5)
print("이름 : {}".format(name))
print("나이 : {}\n성별 : {}".format(age, gender))
print("직업 : {}\n주소 : {}".format(job, addr),end="\n\n")

# Python 스타일 (3.6 이후버전)
print("="*5, "python new style", "="*5)
print(f"이름 : {name}")
print(f"""나이 : {age}
성별 : {gender}
직업 : {job}
주소 : {addr}
""",end="\n\n")

# Java 스타일
print("="*5, "java style", "="*5)
print("이름 : " + name)
print("나이 : " + str(age))
print("성별 : " + gender)
print("직업 : " + job)
print("주소 : " + addr)

# 출력 포맷 정렬
# < : 좌측정렬
# > : 우측정렬
# ^ : 중앙정렬

print("|{:6}|".format(10))
print("|{:<6}|".format(10))
print("|{:>6}|".format(10))
print("|{:^6}|".format(10))

num=10
print(f"|{num:6}|")
print(f"|{num:<6}|")
print(f"|{num:>6}|")
print(f"|{num:^6}|")

# 소수점 이하 자르기
print(f"{3.1415923746:.2f}")

