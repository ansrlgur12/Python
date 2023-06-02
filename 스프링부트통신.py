import requests
import json

data = {
    "id" : "곰돌이사육사",
    "pwd" : "sphb8250"
}

# JSON 데이터를 서버로 전달 
url = "http://localhost:8111/login"
header = {"Content-Type" : "application/json"}

response = requests.post(url, data=json.dumps(data), headers=header)
if response.status_code == 200 :
    print("데이터 전송 완료")
else : print("오류")