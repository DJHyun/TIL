import sys

X = int(sys.stdin.readline().strip())
idx = 1
cnt = 0
result=[]
for i in range(1,X+1):
    cnt = int((i-1)*i*0.5+1)
    if cnt == 1:
        result.append(f'{cnt}/{cnt}')
    elif cnt%2:
        result.append(f'{cnt-1}/{cnt}')
    else:    
        result.append(f'{cnt}/{cnt-1}')

print(result)     
    


        
    