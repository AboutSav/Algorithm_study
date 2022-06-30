import sys
 
n = int(sys.stdin.readline())
*switch, = map(int, sys.stdin.readline().split()) 
 
n2 = int(sys.stdin.readline()) 
 
for _ in range(n2):
    a, b = map(int, sys.stdin.readline().split())   
    if a == 1 :  
        plus = b
        while(b <= n):
            switch[b-1] = 1-switch[b-1] 
            b += plus
    else:  
        switch[b-1] = 1-switch[b-1]
        b1 = b-1
        b2 = b+1 
        while(b1 >= 1 and b2 <= n): 
            if (switch[b1-1] == switch[b2-1]):
                switch[b1-1] = 1-switch[b1-1] 
                switch[b2-1] = 1-switch[b2-1]  
            else: break 
            b1 -= 1
            b2 += 1  

for i in range(0, n, 20):
    print(*switch[i:i+20])
