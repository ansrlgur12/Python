# 고객의 이름 입력 받기
# 행사 제목 입력 받기
# 행사 날짜 입력 받기 : 입력 예) 20300501  // 날짜를 입력 받아 몇월인지 확인하고 그에 맞는 행사 문구 가져와서 출력
# 행사 시간 입력 받기 : 입력 예) 15시      // 시간 입력 받아서 이쁘게 변경하기
# --------------------------------------------------------------
# 한파의 연속인 1월 입니다.
# 봄을 기다리는 2월 입니다.
# 봄의 기운이 느껴지는 3월 입니다.
# 새싹이 피어나는 4월 입니다.
# 계절의 여왕 5월 입니다.  
# 활동하기 좋은 6월 입니다. 
# 휴가가 기다려지는 7월 입니다. 
# 무더운 8월 입니다. 
# 선선한 9월 입니다. 
# 천고마비의 계절 10월 입니다.
# 쓸쓸한 늦가을 11월 입니다.
# 올 한해의 마무리 12월 입니다.
# --------------------------------------------------------------

name = input("이름을 입력하세요 : ")
event_name = input("행사 제목을 입력하세요 : ")
event_date = input("행사 날짜를 입력하세요 : ")
event_time = input("행사 시간을 입력하세요 : ")
event_month = event_date[4:6]

if(event_month == "01") : month_text = "한파의 연속인 1월 입니다."
elif(event_month == "02") : month_text = "봄을 기다리는 2월 입니다."
elif(event_month == "03") : month_text = "봄의 기운이 느껴지는 3월 입니다."
elif(event_month == "04") : month_text = "새싹이 피어나는 4월 입니다."
elif(event_month == "05") : month_text = "계절의 여왕 5월 입니다.  "
elif(event_month == "06") : month_text = "활동하기 좋은 6월 입니다. "
elif(event_month == "07") : month_text = "휴가가 기다려지는 7월 입니다."
elif(event_month == "08") : month_text = "무더운 8월 입니다. "
elif(event_month == "09") : month_text = "선선한 9월 입니다. "
elif(event_month == "10") : month_text = "천고마비의 계절 10월 입니다."
elif(event_month == "11") : month_text = "쓸쓸한 늦가을 11월 입니다."
else : month_text = "올 한해의 마무리 12월 입니다."

trans_time = int(event_time)
if(trans_time > 12) :
    trans_time = trans_time - 12
    time = "오후 " + str(trans_time)
else :
    time = "오전 " + str(trans_time)

print(f"""
안녕하세요 {name}님
{month_text}
아래의 일정으로 {event_name}을 진행하고자 하오니 오셔서
자리를 빛내 주시기 바랍니다.
===== 행사 안내 =====
일시 : {event_date[:4]}년 {event_month}월 {event_date[-2:]}일
시간 : {time}시
""")