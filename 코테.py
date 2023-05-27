# 입력받은 n개의 원소에 대한 평균 구하기
#count = 0
#sum = 0
#while True :
#    num = int(input("정수를 입력하세요 : "))
#    if num == 0 : break
#    count += 1
#    sum += num
#    num = 0
#print(f"정수의 합은 {sum/count}입니다.")


# 정수 n을 입력받아 n * n 출력하기
#n = int(input("정수를 입력하세요 : "))
#print(f"결과 : {n*n}")



# n개에 대한 숫자를 입력받아 최소값 및 최대값 구하기

max_num = 0
min_num = 0
while True :
    num = int(input("정수를 입력하세요 : "))
    if num == 0 : break
    if max_num < num : max_num = num
    else : pass
    if min_num > num : min_num = num
    else : pass
    num = 0
    print(f"""
    최댓값 = {max_num}
    최소값 = {min_num}
    """)



# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기

jumin = input("주민번호를 입력해주세요")