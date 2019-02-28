# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
import sys
sys.stdin = open("숫자추가.txt", "r")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        HeadNode = Node("HEAD")
        self.head = HeadNode
        self.tail = HeadNode
        self.NumOfData = 0

    def insert(self,data):
        insertNode = Node(data)
        self.tail.next = insertNode
        self.tail = insertNode
        self.NumOfData += 1

T = int(input())
for test_case in range(1, 2):
    test = LinkedList()

    print(test.head.next)
    print(test.tail.next)

