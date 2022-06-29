s = input()
res = []
red = []
tag = False
for i in range(len(s)) :
    if s[i] == '<' or s[i] == ' ':
        if red != '':
            res += "".join(reversed(red))
            red.clear()
        if s[i] != ' ':
            tag = True
    if tag == True or s[i] == ' ':
        res.append(s[i])
    else :
        red.append(s[i])
    if s[i] == '>' :
        tag = False
if red != '':
    res += "".join(reversed(red))
print("".join(res))