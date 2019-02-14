# baekjoon source = "https://www.acmicpc.net/problem/2751"

import sys

T = int(sys.stdin.readline())
number = [0]*T

for i in range(T):
    number[i] = (int(sys.stdin.readline()))
    
# def merge_sort(m):
    
#     if len(m) <= 1:
#         return m

#     mid = len(m)//2
#     left = m[:mid]
#     right = m[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)
#     i,j = 0,0
#     result = []
    
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))

#     if left:
#         result.extend(left)
#     if right:
#         result.extend(right)

#     return result

def merge_sort(m):

    if len(m) <= 1:
        return m

    left = merge_sort(m[:len(m)//2])
    right = merge_sort(m[len(m)//2:])

    return merge(left, right)

def merge(left,right):
    
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)
    if right:
        result.extend(right)
    
    return result

for i in (merge_sort(number)):
    print(i)
