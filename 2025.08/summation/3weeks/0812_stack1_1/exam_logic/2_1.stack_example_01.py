"""
스택을 구현한 후, 이를 이용해 3개의 데이터를 저장하고 다시 3번 꺼내어 출력
"""

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
# ___________________ 여기까지는 배열에 하나씩 삽입하는 과정이랑 동일
print('단순 pop연산')
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

# 간단한 스택
print('인덱스 활용한 간단한 스택 pop')

top = -1 # top을 -1로 하는이유는 인덱스가 0 부터 시작하기때문에 아무것도 없음을 나타내는 수임
stack = [0] * 10 # 사이즈가 10인 스택배열 생성

top += 1            # push(1) top이 1 증가 즉 현재 가리키는 인덱스가 증가
stack[top] = 1
top += 1            # push(2)
stack[top] = 2
top += 1            # push(3)
stack[top] = 3
# LIFO구조로 가리키는 곳이 한칸씩 줄면서 나중에 들어온 원소가 pop됨
top -= 1            # pop()
print(stack[top+1])
top -= 1            # pop()
print(stack[top+1])
top -= 1            # pop()
print(stack[top+1])
