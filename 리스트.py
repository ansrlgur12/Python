# 연속적으로 데이터를 저장하는 자료형. 동적으로 크기가 변경 됨. 다른 타입의 데이터를 함께 사용 가능하다(다른 배열, 다른 타입 등)
# 읽고 쓰기가 가능, []

numbers = [1,2,3,4,5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "apple", True, 3.14, [1,2,3,4,5]]

empty = []
str_n = ""

# 변수 사용 대비 이점

# 변수 사용시
# kor, eng, mat = map(int, input("성적 입력 : ").split())
# total = kor + eng + mat
# print(f"평균 : {total // 3}")

# list 사용시
# score = list(map(int, input("성적 입력 : ").split()))
# print(f"{len(score)}과목 성적의 평균 : {sum(score) // len(score)}")

# 이점 : 값이 오류가 날 수 없다 (변수로 지정해놓으면 값이 모자라거나 넘어서는 순간 오류가생김)


print(mixed[1:3]) # 1번 인덱스부터 3번 미만 인덱스까지(1, 2번 인덱스 출력)
s = ["korea", "seoul", "incheon", [1,2,3,4,5], ["안유진", "장원영", "가을", "이서", "리즈"]]
print(s[0][1])
print(s[3][4])
print(s[4][1][1])

# 리스트 연산자 : 연결(+), 반복(*)
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a * 2)
print(list_a + list_b)

# 리스트 요소 추가
# append : 리스트 끝에 값을 추가하는 함수 - O(1)
# insert : 특정 위치에 값을 추가하는 함수 - O(n), 한칸씩 다 이동해야함

list_a.append(4)
list_a.append(10)
list_a.insert(1, 22) # 1번 인덱스에 22를 삽입

print(list_a)
print()
print("-"*25+" 리스트 제거하기 "+"-"*25)

# 리스트 제거하기
# pop : 인덱스가 없으면 마지막 요소 반환하고 삭제(반환하고 삭제 : print 찍어보면 뭐가 삭제되는건지 확인할 수 있음)
#       인덱스가 있으면 인덱스의 위치의 데이터 삭제(인덱스 범위를 벗어나면 에러)
# remove : 값으로 제거, 동일한 값이 여러개 있는 경우 낮은 인덱스부터 제거
# clear : 모든 값을 지우고 빈 리스트만 남김
# del '리스트명'['인덱스'] : 해당 값 제거
 
list_all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "korea"]
print(list_all)
list_all.pop() # 인덱스가 없으므로 마지막 요소 제거
print(f"pop() : {list_all}")
list_all.pop(8)
print(f"pop(8) : {list_all}")
list_all.insert(8,8)
print(f"insert(8,8) : {list_all}")
del list_all[10]
print(f"del list_all[10] : {list_all}")
list_all.clear()
print(f"clear() : {list_all}")

# 중복제거
print()
print("-"*25+" 중복 제거하기 "+"-"*25)
my_list = ["A", "B", "C", "D", "A", "B", "E", "F"]
new_list = []
for e in my_list : # my_list 리스트를 요소값 기준으로 자동 순회
    if e not in new_list :
        new_list.append(e) # 리스트의 끝에 값을 추가하는 함수
print(new_list)

# 정렬
print()
print("-"*25+" 정렬하기 "+"-"*25)
arr = [1, 4, 5, 66, 777, 1000, 234, 456, 56, 678]
arr.sort() # 오름차순
print(arr)
arr.sort(reverse=True) # 내림차순
print(arr)

# 리스트의 모든 요소 탐색하기
print()
print("-"*25+"리스트의 모든 요소 탐색하기"+"-"*25)
name_x = ["안유진", "장원영", "가을", "이서", "리즈"]
for e in name_x : # 자바의 향상for문과 같이 리스트의 요소를 자동 순회
    print(e, end=" ")
print()
for i in range(len(name_x)) : # 리스트의 갯수를 구해서 인덱스로 순회
    print(name_x[i], end=" ")

# 응용문제 : 홀수, 짝수 나누어담기
# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력하는 문제
print()
print("-"*25+"응용문제"+"-"*25)
number = list(map(int, input("입력 : ").split()))
even = [] # 짝수를 저장할 리스트
odd = [] # 홀수를 저장할 리스트

for e in number :
    if e % 2 == 0 : even.append(e)
    else : odd.append(e)

print(f"짝수 : {even}")
print(f"홀수 : {odd}")

# 람다를 이용하는 방법으로 풀기
print()
print("-"*25+"람다 활용"+"-"*25)
number = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda x : x % 2 == 1, number))
even = list(filter(lambda x : x % 2 == 0, number))
print(f"짝수 : {even}")
print(f"홀수 : {odd}")
