import sys

X = int(sys.stdin.readline().strip())
result = [['1/1']]
flag = True
idx = 1
i = 1
while idx < X:
    if len(result) < i:
        if flag:
            result[i-1].append([])
    
    
    
print(result)


        
    