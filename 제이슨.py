# Python Object(Dictionary, List, Tuple 등)를 JSON 문자열로 변경하는 것을 JSON Encoding
# 인코딩은 json.dumps() 메소드를 이용해서 JSON문자열로 변환
# 디코딩은 JSON 문자열을 Python타입(Dictionary, List, Tuple 등)으로 변경하는 것 : json.loads()

import json

# customer = {
#     "id" : 12345,
#     "name" : "곰돌이사육사",
#     "history" : [
#         {"date" : "2023-05-05", "제품" : "iPhone Pro 14"},
#         {"date" : "2023-06-02", "제품" : "Galaxy S23 Ultra"}
#     ]
# }

# jsonString = json.dumps(customer, ensure_ascii=False) # ensure_ascii = False : 한글깨짐현상 해결
# print(jsonString)

import json

jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
    {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
    {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
]}'''

dict = json.loads(jsonString)

print(dict["name"])
for h in dict["history"]:
    print(h["date"], h["item"])