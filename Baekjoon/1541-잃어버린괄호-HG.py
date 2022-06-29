import sys

t = sys.stdin.readline().strip().split('-')
cal = []
for i in t :
    temp = 0
    p = i.split('+')
    for j in p :
        temp += int(j)
    cal.append(temp)
result = cal[0]
for i in range(1, len(cal)) :
    result -= cal[i]

print(result)