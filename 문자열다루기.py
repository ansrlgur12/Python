# 여러줄로 이루어진 문자열을 처리할 때 사용
print('''동해물과 백두산이 마르고 닳도록 하느님이
보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전 하세
''')
print("저의 이름은 '곰돌이사육사'입니다.")
print('저의 이름은 "곰돌이사육사" 입니다.')

# 이스케이프 문자 사용하기
print("서울시\t강남구\t역삼동")
print("사과\r바나나\r오렌지")

# 인덱싱 : 인덱스는 항상 0에서 부터 시작
jumin = "991120-1234567"
print("성별 : " + jumin[7])
print("출생년도 : " + jumin[:2]) # 시작 인덱스를 주지 않으면 0에서 시작하고 end는 미만 개념이 있음
print("월 : " + jumin[2:4]) # 2에서 4미만
print("일 : " + jumin[4:6]) # 4에서 6미만

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

print("안녕하세요"[:2])
print("안녕하세요"[-3:])

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "K" -- 문자열 요소는 변경할 수 없음

# 대소문자 바꾸기
a = "Hello Python Program.."
print(a.upper())
print(a.lower())

# 문자열 변경하기 : replace("","")
input_str = "Hello Python Program"
new_str = input_str.replace("Python", "React")
print(new_str)

# 문자열에 포함된 문자 갯수 세기 및 문자열 길이
# 갯수 세기 : count()
# 길이 반환 : __len__(), len()
print(input_str.count("l")) # "l"문자가 몇번 나오는지 갯수 세기
print(len(input_str)) # len()함수 사용
print(input_str.__len__()) # 문자열에 포함된 내장 함수를 사용

# 문자열 찾기 : fint(), rfind(), index()
# find() : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 찾지 못하면 -1을 반환 # rfind는 뒤에서 부터 찾음
# index() : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 찾지 못하면 ValueError 라는 예외를 발생 시킴
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장")) # 뒤에서 부터 해당 문자열을 찾지만 인덱스는 앞에서부터 계산
print(phrase.index("가장"))

# 없는 문자열 읽기
print(phrase.find("나에게"))
# print(phrase.index("나에게"))

new_pharase = phrase.replace("가장", "나에게")
print(new_pharase)

# 문자열 연산자
# "문자열" + "문자열"
# "문자열" * 3 -- 뒤에 오는 숫자만큼 문자열을 반복
print("A" + "B")
print("a" * 4)

# 문자열의 양옆 공백 제거 : strip()
input_a = """
    안녕하세요.
문자열에 대해서 공부 중 입니다.
"""
print(input_a.strip())
