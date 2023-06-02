import pymysql

# 전역 변수
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# mySQL 연결
conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", db="mysqlDB", charset="utf8")

# 커서 생성
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")
print("-"*50)
print("사용자ID     이름     이메일            출생년도")
print("-"*50)
while True :
    row = cur.fetchone()
    if row == None : break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(f"{data1:12}{data2:5}{data3:21}{data4:5}")
print("-"*50)