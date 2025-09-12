'''
'''
import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T + 1):
    # N : 인원수 k_MIN : 분반최소인원  K_MAX : 분반최대인원
    N, K_MIN, K_MAX = map(int, input().split())
    # N명에 점수 리스트
    SCORE = list(map(int, input().split()))

    class_A = []
    class_B = []
    class_C = []

    for i in range(1, N):
        max_score = 0
        if max_score < SCORE[i]:
            max_score = SCORE[i]
            T2 = max_score
        avg = sum(SCORE) / N
        T1 = round(avg)
    for i in range(N):
        if SCORE[i] >= T2:
            SCORE[i] = 'A'
            class_A.append(SCORE[i])
        elif T1 <= SCORE[i] < T2:
            SCORE[i] = 'B'
            class_B.append(SCORE[i])

        elif T1 > SCORE[i]:
            SCORE[i] = 'C'
            class_C.append(SCORE[i])
    A = len(class_A)
    B = len(class_B)
    C = len(class_C)

    many_person = max(A, B, C)
    min_person = min(A, B, C)

    result = many_person - min_person

    if K_MIN > min_person:
        result = -1



    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d %d" % (t, result))

'''
5
5 1 4 // 첫 번째 테스트 케이스, [표 1-1] [표 1-2] 참고
3 5 5 4 5
6 2 6 // 두 번째 테스트 케이스, [표 2-1] [표 2-2] 참고
5 3 3 5 5 1
7 1 6 // 세 번째 테스트 케이스, [표 3-1] [표 3-2] 참고
3 3 5 2 5 1 2
8 1 7 // 네 번째 테스트 케이스
3 1 1 2 2 5 3 5
10 1 6 // 다섯 번째 테스트 케이스x
4 4 2 4 5 2 5 3 5 5

#1 2
#2 -1 // 반을 편성 할 수 없는 경우, -1 을 출력할 것
#3 1
#4 2
#5 1

'''
