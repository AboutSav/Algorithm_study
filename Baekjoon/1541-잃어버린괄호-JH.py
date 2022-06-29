import sys 
 
poly = (sys.stdin.readline().rstrip().split('-'))  

total = sum(map(int, poly[0].split("+")))  
 
for i in range(1,len(poly)):
    minus = sum(map(int, poly[i].split("+"))) 
    total -= minus
 
print(total)