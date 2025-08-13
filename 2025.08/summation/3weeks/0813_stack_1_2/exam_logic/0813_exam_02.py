"""
팩토리얼 계산
"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))  # 5! = 120
