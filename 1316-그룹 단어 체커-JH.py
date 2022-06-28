import sys 
 
n = int(input()) 
arr = []   
count = 0

for _ in range(n):
    arr.append((sys.stdin.readline().rstrip()))  
 
for i in arr: 
    tmp = [ord(x) - 96 for x in i]  
    cnt = 0
    for j in range(0,len(tmp)-1): 
        if tmp[j] != tmp[j+1]:
            cnt += 1    
    if len(set(tmp))-1 == cnt:
        count += 1 

print(count)