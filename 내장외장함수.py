# 내장 함수 : 파이썬 기본적으로 제공하며, import 없이 사용
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"최대값 : {max(ls)}")
print(f"평균 : {sum(ls) / len(ls)}")
print(f"정렬 : {sorted(ls)}")
print(f"몫과 나머지 : {divmod(sum(ls), 5)}")

# 외장 함수 (import 해서 사용) : 랜덤
import random

# 지정한 범위 내의 임의의 수를 구하는 함수
rand = random.randint(0, 4) # 0 ~ 4 '사이'의 임의의 값이 생성
print(rand)

rand_range = random.randrange(0, 4) # 0 ~ 4 '미만'의 임의의 값이 생성
print(rand_range)

# 현재 시간 가져오기
from datetime import datetime

datetime.today()            # 현재 날짜 가져오기
datetime.today().year        # 현재 연도 가져오기
datetime.today().month      # 현재 월 가져오기
datetime.today().day        # 현재 일 가져오기
datetime.today().hour        # 현재 시간 가져오기

print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)