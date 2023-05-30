# 튜플 : 변경할 수 없는 시퀀스 자료형 입니다. ()괄호를 사용하여 생성 합니다.
# 패킹과 언패킹 개념이 있음 

# [] = 리스트
# {} = 딕셔너리
# () = 튜플
# 괄호없어도 튜플 : ex) person = "곰돌이사육사", 25, "서울", True

# 튜플 정의하기
person = ("곰돌이사육사", 25, "서울") # ()괄호를 생략해도 튜플, 쓰기 불가 특성
#person[0] = "다른이름변경"
#print(person[0])

# 튜플 언패킹 하기 (구조 분해랑 유사함)
#name, age, city = person
#print(name)
#print(age)
#print(city)

# 튜플을 이용한 함수 반환값 다루기
def get_person() : 
    name = "정경수"
    age = 22
    city = "수원"
    return name, age, city
#result = get_person() # 튜플의 패킹 동작
#print(result)

a, b, c = get_person()
#print(b,a,c)

# 기본적인 동작
tp = 1,2,3,4,5,6,7,8,9,10,1,1,2,2,3,3
print(tp.count(3)) # 원하는 데이터의 갯수를 세어주는 함수 (리스트와 동일)
print(tp.index(1)) # 원하는 데이터의 시작 인덱스를 알려줌
print(len(tp)) # 튜플에 포함된 데이터의 갯수를 반환
print(tp.__len__())

# 튜플에서 사용이 안되는것
del tp[0] # 삭제는 안됨
