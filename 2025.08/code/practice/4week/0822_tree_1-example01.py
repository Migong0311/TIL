"""
부모 노드 번호를 인덱스로 사용해서 자식 노드 번호를 저장하는 방법
4
1 2 1 3 3 4 3 5
"""

# 간선의 개수
E = int(input())
N = 5
# 트리 노드 정보를 한줄로 입력
tree = list(map(int, input().split()))

# left_c[i] -> i번 노드의 왼쪽 자식 노드번호
left_c = [0] * (N + 1)
# right_c[i] -> i번 노드의 오른쪽 자식 노드번호
right_c = [0] * (N + 1)

for i in range(E):
    p = tree[i * 2]  # 부모노드번호
    c = tree[i * 2 + 1]  # 자식노드번호

    # p번 노드의 왼쪽 자식이 없으면 c를 p의 자식으로
    if left_c[p] == 0:
        left_c[p] = c
    else:
        right_c[p] = c

print("부모 : ", *list(range(N+1)))
print()
print('왼쪽 자식: ', *left_c)
print('오른쪽 자식: ', *right_c)
"""
출력
부모 :     0 1 2 3 4 5

왼쪽 자식:  0 2 0 4 0 0
오른쪽 자식: 0 3 0 5 0 0
"""