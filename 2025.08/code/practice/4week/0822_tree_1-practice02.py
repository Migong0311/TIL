import sys

# 표준 입력을 파일로 대체 (input.txt에서 입력을 받음)
sys.stdin = open('input.txt', 'r')


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

A.left = D
A.right = E
E.left = B
E.right = C


def preorder(t):
    if t:
        print(t.value, end="  ")
        preorder(t.left)
        preorder(t.right)


preorder(A)

