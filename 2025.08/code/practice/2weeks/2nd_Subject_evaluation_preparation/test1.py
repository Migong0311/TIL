'''
":key
파리퇴치문제 연습
'''
import sys

sys.stdin = open('input.txt', 'r')

# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_fly = 0
#
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             fly_sum = 0
#             for di in range(M):
#                 for dj in range(M):
#                     fly_sum += arr[i + di][j + dj]
#
#             if max_fly < fly_sum:
#                 max_fly = fly_sum
#
#     print(f'#{t} {max_fly}')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_sum = 0
            for di in range(M):
                for dj in range(M):
                    fly_sum += arr[i + di][j + dj]

            if max_fly < fly_sum:
                max_fly = fly_sum

    print(f'#{t} {max_fly}')

"""
#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242
"""
