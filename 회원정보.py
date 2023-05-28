# 이름 입력
# 나이 입력 : 1~199 까지 입력 받고 잘못된 값이 오면 재 입력을 요청한다.
# 성별 입력 : 영문자(M과 m은 남성, F와 f는 여성)로 입력 받고 나머지는 재입력을 요청한다.
# 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직) 으로 입력받고 나머지는 재입력 요청한다.
# 결과는 마지막에 한번에 출력한다.

name = input("이름을 입력하세요 : ")
while True:
#    age = int(input("나이를 입력하세요 : "))
#    if age < 0 or age > 199 : 
#        print("나이를 다시 입력해주세요")
#        continue
#    else : break

    age = input("나이를 입력하세요 : ")
    if age.isdigit() : #입력 받은 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200 : break
    print("다시 입력해주세요")


while True:
    input_gender = input("성별을 입력해주세요(M/F) : ")
    if input_gender == "M" or input_gender == "m" :
        gender = "남성"
        break
    elif input_gender == "F" or input_gender == "f" :
        gender = "여성"
        break
    else : 
        print("다시 입력해주세요")
        continue

while True:
    input_job = int(input("직업을 입력하세요 (1. 학생  2. 회사원  3. 주부  4. 무직) : "))
    if input_job == 1 : 
        job = "학생"
        break
    elif input_job == 2 :
        job = "회사원"
        break
    elif input_job == 3 :
        job = "주부"
        break
    elif input_job == 4 :
        job = "무직"
        break
    else : 
        print("다시 입력해주세요")
        continue


print(f"""
이름 : {name}
나이 : {age}
성별 : {gender}
직업 : {job}
""")