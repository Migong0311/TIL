"""
자식 노드 번호를 인덱스로 사용해서 부모 노드 번호를 저장하는 방법

입력
4
1 2 1 3 3 4 3 5
"""

E = int(input())
N = 5

tree = list(map(int, input().split()))

parent = [0] * (N + 1)

for i in range(E):
    p = tree[i * 2]  # 부모노드번호
    c = tree[i * 2 + 1]  # 자식노드번호

    parent[c] = p

print("자식 : ", *list(range(N + 1)))
print()
print('부모 : ', *parent)
"""
출력
자식 :  0 1 2 3 4 5
부모 :  0 0 1 1 3 3
"""
'''
루트찾기 , 조상찾기
'''
child = 5

ancestor = []

while parent[child] != 0:
    child = parent[child]
    ancestor.append(child)

    root = child
print(f'루트번호 : {root},조상번호 : {ancestor}')
# 출력 : 루트번호 : 1,조상번호 : [3, 1]
