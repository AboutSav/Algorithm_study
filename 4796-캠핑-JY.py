def camp_schedule(L,P,V) :
    rest = V % P # 떨거지들
    al = V - rest
    if rest > L : # L이 더 작으면 떨거지중 L만 추가
        return ((al // P) * L) + L
    else :
        return ((al // P) * L) + rest # 떨거지 뺀 거에서 P기간 별로 나누고 갈 수 있는 L만큼 더하기 + 떨거지

arr = []
count = 0
while(1) :
    arr.append(list(map(int, input().split())))
    if(sum(arr[count]) == 0) :
        arr.pop()
        break
    count += 1

for j in range(len(arr)) :
    res = camp_schedule(arr[j][0],arr[j][1],arr[j][2])
    print("Case",str(j + 1)+":", res)