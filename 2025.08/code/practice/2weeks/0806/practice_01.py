import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 대각선의 합 구하기
    s = 0
    # 우하향 대각선
    for i in range(N):
        s += arr[i][i]
    # 좌하향 대각선

    for i in range(N):
        s += arr[i][N - 1 - i]
    # 겹치는 부분 존재
    s -= arr[N // 2][N // 2]

    print('#', t, s)
