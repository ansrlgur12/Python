result = ""
for e in input() :
    if e.islower() :
        result += e.upper()
    else : 
        result += e.lower()
print(result)