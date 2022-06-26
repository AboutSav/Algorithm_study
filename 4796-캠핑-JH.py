import sys

list = [] 

while True :
    L, P, V = map(int, sys.stdin.readline().split())  
    if L ==0 and P == 0 and V == 0 :
        break 
    q = V // P 
    r = min((V % P), L)  
    list.append(L*q+r)
    
for i in range(0, len(list)):
    print("Case "+str(i+1)+":",list[i])
