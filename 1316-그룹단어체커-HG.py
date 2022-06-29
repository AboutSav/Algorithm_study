import sys
T = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(T)]

for i in data :
  temp = ""
  test = []
  for a in range(len(i)) :
    if i[a] == temp :
      continue
    if i[a] in test :
      T -= 1
      break
    temp = i[a]
    test.append(i[a])
print(T)