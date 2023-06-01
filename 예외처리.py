# 예외처리란? 실행도중에 발생하는 문제를 처리하기 위해서 사용 (회피가능한 문제에 대해서 처리)
try : 
    print("나눗셈 계산기 입니다.")
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("두번째 숫자 입력 : "))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError :
    pass
except ZeroDivisionError as err :
    pass
except Exception as err :
    print(err)
else :
    print("정상 처리 되었습니다")
finally :
    print("프로그램 종료!")

# try : 
#     score_file = open("score11.txt", "r", encoding="utf8")
#     print(score_file.read())
#     score_file.close()
# except FileNotFoundError :
#     pass

