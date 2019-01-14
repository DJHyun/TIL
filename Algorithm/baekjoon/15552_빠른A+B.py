import sys

for T in range(int(sys.stdin.readline())):
    numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    print(sum(numbers))

        