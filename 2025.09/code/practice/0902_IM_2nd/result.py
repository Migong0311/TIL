import sys

sys.stdin = open('input.txt', 'r')

# 입력은 input()만 사용 (파일 리다이렉트가 필요하면 외부에서 처리)
T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):  # 테스트 케이스 반복
    N, K_MIN, K_MAX = map(int, input().split())  # N, 최소/최대 인원
    scores = list(map(int, input().split()))  # 점수 배열 (길이 N)

    # [수정] 원래 로직: T2를 '최대값', T1을 '평균 반올림'으로 고정
    #  - 이렇게 하면 가능한 분할 대부분을 놓침
    #  - 또한 scores를 'A/B/C' 문자로 덮어써 원본 손실
    # [수정] 변경 내용: 모든 (T1, T2) 조합을 전수 탐색하고, 점수는 건드리지 않음

    # [수정] 1) 점수 범위(1..100) 기반 빈도 배열
    freq = [0] * 101  # freq[v] = 점수 v의 개수
    for x in scores:  # 점수를 훼손하지 않고 빈도만 집계
        freq[x] += 1

    # [수정] 2) 누적합(prefix): ps[s] = (점수 ≤ s)의 인원 수
    ps = [0] * 101
    for s in range(1, 101):
        ps[s] = ps[s - 1] + freq[s]

    best_diff = None  # 정답 후보 (최소 차이)

    # [수정] 3) 모든 (T1, T2) 전수 탐색: 1 ≤ T1 < T2 ≤ 100
    for T1 in range(1, 100):  # T1은 1..99
        C_cnt = ps[T1 - 1]  # C = (< T1)
        # [수정] 가지치기: C는 T2와 무관하므로 미리 범위 검증
        if not (K_MIN <= C_cnt <= K_MAX):
            continue

        for T2 in range(T1 + 1, 101):  # T2는 (T1+1)..100
            B_cnt = ps[T2 - 1] - ps[T1 - 1]  # B = [T1, T2-1]
            A_cnt = N - ps[T2 - 1]  # A = [T2, 100]

            # [수정] 각 반 인원 제한 검사
            if not (K_MIN <= A_cnt <= K_MAX):  # A 반 인원 검사
                continue
            if not (K_MIN <= B_cnt <= K_MAX):  # B 반 인원 검사
                continue
            # C_cnt는 위에서 이미 검사됨

            # [수정] 차이 계산 및 최소값 갱신
            mx = A_cnt
            if B_cnt > mx:  # 최대값 수동 계산
                mx = B_cnt
            if C_cnt > mx:
                mx = C_cnt

            mn = A_cnt
            if B_cnt < mn:  # 최소값 수동 계산
                mn = B_cnt
            if C_cnt < mn:
                mn = C_cnt

            diff = mx - mn
            if best_diff is None or diff < best_diff:
                best_diff = diff

    # [수정] 유효 분할이 하나도 없으면 -1
    ans = best_diff if best_diff is not None else -1

    print(f"#{tc} {ans}")  # 형식에 맞게 출력
