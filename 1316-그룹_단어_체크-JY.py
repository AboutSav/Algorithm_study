def groupWord(word) :
    save = []
    pre = ''
    for i in range(len(word)) :
        if word[i] in save and pre != word[i]:
            return False
        else :
            save.append(word[i])
            pre = word[i]
    return True
count = 0
N = int(input())
for i in range(N) :
    if groupWord(input()) == True :
        count += 1
print(count)