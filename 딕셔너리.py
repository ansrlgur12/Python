# # 키와 값이 존재하는 자료 구조(자바의 Map과 유사) {}
# # 키와 값의 구분은 :(콜론)
# coffee_menu = {"Americano" : 2500, "Espresso" : 2300, "Latte" : 4500}
# tea_menu = {"Black tea" : 4000, "Green tea" : 4000}
# food_menu = {"Cake" : 5000}
# 
# print(coffee_menu)
# 
# # 키 값으로 값을 확인하기
# print(coffee_menu["Americano"])
# 
# # get 함수로 값 확인하기
# print(coffee_menu.get("Americano"))
# 
# # 딕셔너리[키] = 값 : 새로운 키와 값을 추가
# # del 딕셔너리[키] : 키로 값을 삭제
# # if key in 딕셔너리 : 키 존재여부 확인
# # 딕셔너리[키] or 딕셔너리.get(키) : 키로 값 확인
# # update 함수 : 딕셔너리의 데이터를 한꺼번에 변경할 때 사용
# # keys() : 딕셔너리에서 키를 가져옴
# # values() : 딕셔너리에서 값을 가져옴
# 
# dict1 = {"자바": 80, "리액트": 90, "파이썬": 88}
# print(dict1.keys()) # 키를 가져옴
# print(dict1.values()) # 값을 가져옴
# print(dict1.items())
# 
# # 키 존재 여부 확인 : True, False로 반환
# print("리액트" in dict1)
# print("자바스크립트" in dict1)
# 
# # 키 값으로 값을 반환 받음
# # print(dict1["자바스크립트"]) # 에러 발생함
# 
# # 반복문과 함께 사용하기
# for key in coffee_menu : # 딕셔너리를 키값 기준으로 자동 순회
#     print(key, ":", coffee_menu[key])

menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."] 
}

while True :
    print("메뉴를 선택하세요")
    menu = input("[1]보기 [2]조회 [3]추가 [4]삭제 [5]종료 : ")
    if menu == "1" :
        for key in menu_dic :
            print(key, ":", menu_dic[key])
    elif menu == "2" :
        rtrv_name = input("조회 할 메뉴 명을 입력하세요 : ")
        if rtrv_name in menu_dic :
            print(menu_dic[rtrv_name])
        else : print("찾는 메뉴가 없습니다.")
    elif menu == "3" :
        add_name = input("추가 할 메뉴를 입력하세요 : ")
        if add_name not in menu_dic :
            grp = input("카테고리 입력 : ")
            price = int(input("가격 입력 : "))
            desc = input("설명을 입력하세요 : ")
            menu_dic[add_name] = [grp, price, desc] # 새로운 키로 값을 추가하기
        else : print("이미 존재하는 메뉴 입니다.")
    elif menu == "4" :
        del_menu = input("삭제할 메뉴를 입력 하세요 : ")
        if del_menu in menu_dic :
            del menu_dic[del_menu]
        else : print("존재하지 않는 메뉴입니다.")
    elif menu == "5" :
        print("영업을 종료합니다.")
        break
    else : print("잘 못 입력 하셨습니다.")