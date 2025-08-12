"""
스택을 구현한 후, 이를 이용해 3개의 데이터를 저장하고 다시 3번 꺼내어 출력
"""

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
# ___________________ 여기까지는 배열에 하나씩 삽입하는 과정이랑 동일
print('단순 pop연산')
print()
print()
print(stack.pop())
print(stack.pop())
print(stack.pop())
print()
print()

'''
pop 메서드를 통해 stack배열의 가장 나중에 들어간 원소부터 차례대로 출력이된다

[출력]
3
2
1
'''

# 스택 크기
size = 10
stack = [0] * size  # 스택 저장소
top = -1  # 스택의 맨 위 인덱스


# push 함수: 스택에 데이터를 추가
def push(item):
    global top
    if top >= size - 1:  # 스택이 가득 찼는지 확인
        print("스택 오버플로우! 더 이상 추가 불가")
    else:
        top += 1
        stack[top] = item
        print(f"Push: {item} → 현재 스택: {stack[:top + 1]}")


# pop 함수: 스택에서 데이터를 꺼냄
def pop():
    global top
    if top == -1:  # 스택이 비었는지 확인
        print("스택 언더플로우! 꺼낼 데이터 없음")
        return None
    else:
        item = stack[top]
        top -= 1
        print(f"Pop: {item} → 현재 스택: {stack[:top + 1]}")
        return item


# 테스트
push(10)
push(20)
push(30)

pop()
pop()
pop()
pop()  # 빈 스택에서 꺼내기 테스트
