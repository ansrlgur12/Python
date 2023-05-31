# 입력받은 수가 소수인지 아닌지 판별하기(함수 이용)
# 소수란? 1과 자기 자신 이외에 나누어지지 않는 수

# num = int(input("정수를 입력하세요 : "))
# cnt = 0
# def sosu(num) :
#     global cnt
#     for i in range(2, num+1) :
#         if num % i == 0 : cnt += 1
#     if cnt == 1 : print(f"소수입니다.")
#     else : print(f"소수가 아닙니다.")


# sosu(num)


n = int(input("정수 입력 : "))
def is_prime(n) :
    for i in range(2,n) : # 1과 자기자신을 제외
        if n % i == 0 : print(f"{n}은 소수가 아닙니다.")
    print(f"{n}은 소수입니다.")
is_prime(n)
