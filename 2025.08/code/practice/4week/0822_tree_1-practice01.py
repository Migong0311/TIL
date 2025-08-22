import sys

# 표준 입력을 파일로 대체 (input.txt에서 입력을 받음)
sys.stdin = open('input.txt', 'r')

"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

# 트리 노드의 수 (정점 개수)
N = int(input())

# 트리 정보 -> 두 개씩 끊어 읽으면 (부모, 자식) 관계
tree = list(map(int, input().split()))

# 부모 노드 번호를 인덱스로 활용하기 위해
# 왼쪽, 오른쪽 자식 배열을 준비
c_left = [0] * (N + 1)
c_right = [0] * (N + 1)

# (N-1)개의 간선 정보를 바탕으로 트리 구성
for i in range(N - 1):
    p = tree[i * 2]  # 부모 노드 번호
    c = tree[i * 2 + 1]  # 자식 노드 번호

    # p번 노드의 왼쪽 자식이 비어 있으면 왼쪽에 배치
    if c_left[p] == 0:
        c_left[p] = c
    # 이미 왼쪽 자식이 있다면 오른쪽 자식으로 배치
    else:
        c_right[p] = c

# 왼쪽 자식 배열 출력
print(c_left)
# 오른쪽 자식 배열 출력
print(c_right)


# -------------------------------
# 전위 순회 함수 (Preorder: VLR)
# -------------------------------
def preorder(t):
    if t:  # 노드가 존재하면
        print(t, end=' ')  # 현재 노드 방문
        preorder(c_left[t])  # 왼쪽 서브트리 방문
        preorder(c_right[t])  # 오른쪽 서브트리 방문


# -------------------------------
# 중위 순회 함수 (Inorder: LVR)
# -------------------------------
def inorder(t):
    if t:  # 노드가 존재하면
        inorder(c_left[t])  # 왼쪽 서브트리 방문
        print(t, end=' ')  # 현재 노드 방문
        inorder(c_right[t])  # 오른쪽 서브트리 방문


# -------------------------------
# 후위 순회 함수 (Postorder: LRV)
# -------------------------------
def postorder(t):
    if t:  # 노드가 존재하면
        postorder(c_left[t])  # 왼쪽 서브트리 방문
        postorder(c_right[t])  # 오른쪽 서브트리 방문
        print(t, end=' ')  # 현재 노드 방문


print("=== Traversal Results ===")  # 전체 구분선

# 전위 순회
print("\n[Preorder]")
preorder(1)   # 루트(1)부터 전위 순회 시작
print()       # 줄바꿈

# 중위 순회
print("\n[Inorder]")
inorder(1)    # 루트(1)부터 중위 순회 시작
print()       # 줄바꿈

# 후위 순회
print("\n[Postorder]")
postorder(1)  # 루트(1)부터 후위 순회 시작
print()       # 줄바꿈

print("=========================")  # 끝 구분선
