# 입력받은 수가 소수인지 아닌지 판별하기(함수 이용)

num = int(input("정수를 입력하세요 : "))
cnt = 0
def sosu(num) :
    global cnt
    for i in range(2, num+1) :
        if num % i == 0 : cnt += 1
    if cnt == 1 : print(f"소수입니다.")
    else : print(f"소수가 아닙니다.")


sosu(num)

