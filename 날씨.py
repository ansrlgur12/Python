import datetime

timestamp = 1686168515

# 서울의 표준 시간대를 설정합니다.

# 타임스탬프를 datetime 객체로 변환합니다.
dt = datetime.datetime.fromtimestamp(timestamp)


print(dt)