import sys 
   
count = 0

n, *arr = map(str,sys.stdin.read().split())
 
for i in arr: 
    tmp = list(i) 
    cnt = 0
    for j in range(0,len(tmp)-1): 
        if tmp[j] != tmp[j+1]:
            cnt += 1    
    if len(set(tmp))-1 == cnt:
        count += 1 

print(count)