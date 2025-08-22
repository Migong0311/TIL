# 노드 클래스 정의
class Node:
    def __init__(self, item):
        self.item = item  # 노드 값 저장
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드


# 방문 시 출력 함수
def visit(node):
    print(node.item, end=' ')


# 전위 순회
def preorder_traverse(T):
    if T:  # T가 None이 아닐 때 실행
        visit(T)  # ① 현재 노드 방문
        preorder_traverse(T.left)  # ② 왼쪽 서브트리 순회
        preorder_traverse(T.right)  # ③ 오른쪽 서브트리 순회


# 중위 순회
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)  # ① 왼쪽 서브트리 순회
        visit(T)  # ② 현재 노드 방문
        inorder_traverse(T.right)  # ③ 오른쪽 서브트리 순회


# 후위 순회
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)  # ① 왼쪽 서브트리 순회
        postorder_traverse(T.right)  # ② 오른쪽 서브트리 순회
        visit(T)  # ③ 현재 노드 방문


# 🔹 트리 생성 예시
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

# 🔹 순회 실행
print("전위 순회:", end=" ")
preorder_traverse(root)  # 출력: A B D E C F G
print("\n중위 순회:", end=" ")
inorder_traverse(root)  # 출력: D B E A F C G
print("\n후위 순회:", end=" ")
postorder_traverse(root)  # 출력: D E B F G C A