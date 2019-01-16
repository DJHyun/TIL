import math

T = int(input())
k = int(math.log(T//3,2))
print(k)
star = ['  *',' * *','*****']

for i in range(3,T):
    star.append(" "*(T)+star[i%3])
    
for i in range(T):
    print(star[i])   

    


 