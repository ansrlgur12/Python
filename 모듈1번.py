# from math import sin, cos, tan, floor, ceil
# import math as m

# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.floor(2.5))
# print(m.ceil(2.5))

import os
import sys # 시스템 관련 정보를 가지고 있는 모듈
print("명령줄 인수 : ", sys.argv)

# 스크립트 실행 경로 
print("실행 경로 : ", sys.path[0])

# 프로그램 종료
# sys.exit(0)

# 현재 작업 디렉토리 가져오기
cwd = os.getcwd()
print("현재 작업 디렉토리 : ", cwd)

# 파일 존재 여부확인
is_file = os.path.isfile('test.py')
print(is_file)

# 시스템 명령어 출력
os.system("dir")