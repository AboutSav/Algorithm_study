swn = int(input())
sarr = list(map(int,input().split(' ')))
stn = int(input())
ss = []
for i in range(stn) :
    ss.append(list(map(int,input().split())))
for i in range(stn) :
    if ss[i][0] == 1: #남학생
        for j in range(1,swn + 1) :
            if j % ss[i][1] == 0 :
                sarr[j - 1] = 1 - sarr[j - 1]
    elif ss[i][0] == 2: #여학생
        d = ss[i][1]
        q = 1
        sarr[d - 1] = 1 - sarr[d - 1]
        while(d - q > 0 and d + q < swn + 1 and sarr[d + q - 1] == sarr[d - q - 1]) :
            sarr[d - q - 1] = 1 - sarr[d - q - 1]
            sarr[d + q - 1] = 1 - sarr[d + q - 1]
            q += 1
for i in range(swn) :
    print(sarr[i], end='')
    if i > 0 and i % 19 == 0 :
        print()
    else :
        if i != swn - 1 :
            print(' ', end='')