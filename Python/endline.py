def solution(s):
    result = ''
    while(len(result) != 1):
        result = ''
        print(s)
        first = s[0]
        for i in s[1:]:
            if i == first:
                result += i
            else:
                if (first == 'G' or first == 'B') and (i == 'B' or i=='G'):
                    first = i
                    result += 'R'
                elif (first == 'G' or first == 'R') and (i =='R' or i =='G'):
                    first = i
                    result += 'B'
                elif (first == 'B' or first == 'R') and (i == 'R' or i == 'B'):
                    first = i
                    result += 'G'
        s = result
    return result
        
cset = set('GBR')
def gogo(s):
    while(len(s) > 1):
        s = [x if x == y else (cset - {x,y}).pop() for x,y in zip(s,s[1:])]
    return s 
# print(solution('RRR')) 
# print(solution('RG')) 
# print(solution('RRRGGGBBBBBB')) 
print(gogo('RRGBRGBB')) 