cnt = int(input("통화 횟수 : "))
call_time = list(map(int, input("통화 시간 : ").split()))
y_pay = m_pay = 0

for i in range(cnt) :
    y_pay += (call_time[i] // 30) * 10 + 10
    m_pay += (call_time[i] // 60) * 15 + 15

if y_pay > m_pay :
    print("M", m_pay)
elif y_pay < m_pay :
    print("Y", y_pay)
else :
    print("Y M", y_pay)