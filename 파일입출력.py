# 파이썬에서 기본 입출력 함수는 input()과 print()가 있다.
# 사용자가 터미널을 통한 입출력이 아닌 파일을 통한 입출력을 하기 위해서는 별도의 함수를 사용한다.

# 파일 쓰기 : 파일객체 = open(파일명, 파일모드, 인코딩)
# score_file = open("score.txt", "w", encoding="utf8") # w : write, r : read, a : append
# score_file.write("국어 : 90 \n")
# score_file.write("수학 : 50 \n")
# print("영어 : 67", file=score_file)
# print("과학 : 77", file=score_file)
# score_file.close()

# 파일 읽기
# read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 한줄 씩 내용을 읽음, EOF(End Of File)에 도달하면 None을 반환
# readlines() : 해당 파일의 모든 라인을 순서대로 읽어들임

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# while True :
#     line = score_file.readline()
#     if not line : break
#     print(line, end="")
# score_file.close()

# lines = score_file.readlines()
# print(lines)
# for line in lines :
#     print(line, end="")
# score_file.close()

# with 키워드 : 프로그램이 길어지면 open()과 close() 사이에 많은 코드가 들어가 close를 호출하지 않는 문제가 발생할 수 있음
# with open("score.txt", "r", encoding="utf8") as score_file :
#     print(score_file.read())

# from datetime import datetime
# with open("password.txt", "a") as fd:
#     date = str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day)
#     while True :
#         url = input("사이트 : ")
#         if  url == "exit" : break
#         my_str = url.replace("http://", "")
#         my_str = my_str[:my_str.index(".")] # 슬라이싱 , 처음부터 '.' 위치 미만까지
#         password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + date + "!" + "jks"
#         fd.write(password + "\n")

# pickle : 파이썬 객체를 직렬화(serialize)하고 역직렬화(deserialize)하기 위한 모듈
# 객체를 바이너리 형태로 저장 및 복원하기 위해서 사용
import pickle
data = {"name" : "곰돌이사육사", "age" : 22, "city" : "수원시"}
with open("data.pickle", "wb") as fd :
    pickle.dump(data, fd) # 직렬화해서 파일을 저장합니다.

print(fd)

# 파일에서 객체를 역직렬화해서 복원하기
with open("data.pickle", "rb") as fd :
    restored_data = pickle.load(fd)
print(restored_data)