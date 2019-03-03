# baekjoon source = "https://www.acmicpc.net/problem/2751"
import sys
from fractions import Fraction
T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int,sys.stdin.readline().split())

    while a != 1:
        c = b//a + 1
        d = Fraction(a,b) - Fraction(1,c)

        a = d.numerator
        b = d.denominator

    print(b)