T = int(input())
idx = 0
cnt = 0
k = T//3

for t in range(T):
    if (t != 0 and t % 3 == 0):
        idx += 1

    if idx == 0:   
        if (t % 3 == 0):
            print('*'.rjust(T))
        elif (t % 3 == 1):
            print('* *'.rjust(T+1))
        else:
            print('*****'.rjust(T+2))
    elif idx == 1:
        if (t % 3 == 0):
            print('*'.rjust(T-3),'*'.rjust(5))
        elif (t % 3 == 1):
            print('* *'.rjust(T+1-3),'* *'.rjust(5))
        else:
            print('*****'.rjust(T+2-3),'*****'.rjust(1))
        
    
       


