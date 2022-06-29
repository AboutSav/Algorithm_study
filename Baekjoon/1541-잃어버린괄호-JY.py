import re
def gwalho(g) :
    r = []
    res = 0
    so = 0
    k = True # true 는 양
    for i in range(len(g)) :
        if g[i] == '+' :
            if k == False :
                so += int("".join(r)) * -1
            else :
                res += int("".join(r))
                k = True
            r.clear()
        elif g[i] == '-' :
            if k == False:
                so += int("".join(r)) * -1
            else:
                res += int("".join(r))
                k = False
            r.clear()
        else :
            r.append(g[i])
    if k == False:
        so += int("".join(r)) * -1
    else:
        res += int("".join(r))
    return res + so

getSick = input()
print(gwalho(getSick))