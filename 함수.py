# 함수 : 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램을 의미
# 함수의 사용 목적은 재사용성과 모듈화를 위해 사용(ex) 레고)
# 업무 분장의 기준으로 삼을 수 있으며, 단위 테스트의 기준이 됨
# 일반적으로 함수는 식별자 뒤에 ()가 있음
# 매개변수와 함수를 호출하는 인자의 개수는 일치해야함


# 매개변수가 있고 반환타입이 없는 함수
# def name_card(name, addr, phone) : 
#     print(f"주소 : {addr}")
#     print(f"전화번호 : {phone}")
#     print(f"이름 : {name}")
#     print("-"*30)

# name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678")
# name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999")
# name_card("가을", "수원시 권선구 권선동", "010-1234-1111")

# 은행 계좌 개설하고 입금과 출금 예제
# def open_account(name) :
#     print(f"\"{name}\"님의 계좌가 개설 되었습니다.")
#     return name
# 
# def deposit(balance, input) : # 잔액과 입금 금액을 입력 받음
#     print(f"{input}원이 입금 되었습니다. 잔액은 {balance + input}원 입니다.")
#     return balance + input
# 
# def withdraw(balance, input) :
#     if balance >= input : 
#         print(f"{input}원이 출금 되었습니다. 잔액은 {balance - input}원 입니다.")
#         return balance - input
#     else :
#         print(f"잔액이 부족해 출금이 실패했습니다.")
#         return balance
#     
# balance = 0 # 외부에서 선언하지만 매개변수로 전갈 함
# name = open_account("곰돌이 사육사")
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}의 잔액은 {balance}원 입니다")
# 
# # 기본값 인자 : 함수 선언 시 매개변수에 대한 기본값을 정의할 수 있습니다.
# def profile(name, year = 2, age = 18, school = "태양고") :
#     print(f"이름 : {name},  학교 : {school}, 학년 : {year}, 나이 : {age}")
# 
# profile("나희도")
# profile("고유림")
# profile("백이진", None, 22)

# 가변 매개 변수 : 함수의 매개변수 앞에 (*) 붙여주면 함수의 매개변수를 몇개를 입력하던 함수 내에서 튜플로 인식
# def profile(name, age, *lang) :
#     print(f"이름 : {name}, 나이 : {age}", end= " ")
#     for e in lang :
#         print(e, end=" ")
#     
#     print()
# 
# profile("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile("조세호", 38, "Python", "Java")
# profile("유재석", 48, "Python", "Java", "C", "C++")

# 지역변수와 전역변수
# 전역변수 : 함수보다 변수의 생존범위가 더 넓어서 리턴값이 필요없음
# global 키워드를 사용하면 전역으로 선언한 변수를 함수 내에서 사용할 수 있음

# knife = 10 # 칼을 10자루 준비함
# def game(player) :
#     global knife
#     knife -= player # 게임에 참가한 선수가 사용한 갯수만큼 차감
#     print(f"남아있는 칼은 {knife}자루 입니다.")
# 
# def game2(player, knife) :
#     knife -= player
#     print(f"남아있는 칼은 {knife}자루 입니다.")
# 
# player = int(input("경기에 참여하는 선수 인원 수 : "))
# game2(player, knife)

# 람다와 함수
# 람다 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현, 이름없는 함수를 의미
def add(a,b) : 
    return a+b
print(add(10,20))

print((lambda a, b : a + b)(10,20))

def power(n) :
    return n * n

input = [1,2,3,4,5,6,7,8,9,10]
square = lambda x : x * x

output = list(map(square, input))
print(output)
