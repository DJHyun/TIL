def solution(x):
    flag = True
    low = (x-1)
    high = x
    lowq = 0
    highq = 0
    cnt = 0

    while True:
        if(lowq != 0 and round(lowq,3) == round(highq,3)):
            break

        if ((high+low)/2)**2 > 2:
            high = (high+low)/2
        else:
            low = (high+low)/2
                
        highq = high**2
        lowq = low**2
        cnt +=1

    return(round(low,3))

print(solution(2))


