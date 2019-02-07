import sys
sys.stdin = open("회문2.txt", "r")


def my_palindrome(a):
    for i in range(len(a) // 2):
        if a[i] != a[len(a) - 1 - i]:
            return False
    return True


for test_case in range(1,11):
    input()
    sh = []
    sv = []
    result = 0

    for i in range(100):
        sh.append(list(input()))
    for i in range(100):
        sv.append([])
        for j in range(100):
            sv[i].append(sh[j][i])
    for i in sh:
        for j in range(len(i)):
            for d in range(j+1, len(i)):
                if my_palindrome(i[j:d+1]):
                    if result < ((d - j) + 1):
                        result = ((d - j) + 1)
    for i in sv:
        for j in range(len(i)):
            for d in range(j+1, len(i)):
                if my_palindrome(i[j:d+1]):
                    if result < ((d - j) + 1):
                        result = ((d - j) + 1)
    print(f'#{test_case} {result}')
