# 객체 소속이 아니고 클래스 소속 메소드

class Person :
    count = 0
    def __init__(self) :
        Person.count += 1

    @classmethod
    def print_count(cls) : # cls로 클래스 속성에 접근
        print(f"{cls.count}명이 생성되었습니다.")

곰돌이1번 = Person()
곰돌이2번 = Person()
곰돌이3번 = Person()

Person.print_count()
