a, b, c = map(int, input("정수 3개를 입력하세요 : ").split())
ls = list(str(a * b * c))
print(a*b*c)
for i in range(10) : # i는 0부터 9까지
    if ls.count(str(i)) == 0 : continue
    print(f"{i}는 {ls.count(str(i))}번")