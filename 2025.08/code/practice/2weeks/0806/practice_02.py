import sys

sys.stdin = open("input.txt", "r")

sys.stdout = open("output2.txt", "w")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 전체 위치에서 절대값 차이의 합
    total = 0

    # 델타배열 준비
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            # 현재위치가 행번호 : i, 열번호 : j
            # 현재 위치에 있는 숫자 : num
            num = matrix[i][j]

            # 현재 위치 기준 이웃한 요소들과 차의 절대갑의 합
            abs_sum = 0

            # 상하좌우 요소 탐색하며 현재 위치에 있는 숫자와 차의 절대값 구하기
            for d in range(4):
                # 이동후 행 번호(ni) = 현재 행 번호(i) + d 방향으로 이동했을때 i의 변화량(di[d])
                ni = i + di[d]
                # 이동후 열 번호(nj) = 현재 열 번호(j) + d 방향으로 이동했을때 j의 변화량(dj[d])
                nj = j + dj[d]

                # 주의할점 : 0,0 에서 위로 이동하면 -1,0인데 이것은 유효한 위치(좌표)가 아님
                # 그래서 이동한 후에 인덱스(위치)가 유효한지 검사를 반드시 해야한다.
                if 0 <= ni < N and 0 <= nj < N:
                    # 차 구하기 = 현재 위치에 있는 숫자 - ni,nj 에 있는 숫자
                    sub = num - matrix[ni][nj]
                    # 음수면 양수로
                    if sub < 0:
                        sub = -sub

                    # 절대값 더하기
                    abs_sum += sub

            # 현재 위치 기준 델타탐색이 끝나면 i,j 위치 기준 차의 절대값 함 구하기가 완료되었다.
            total += abs_sum

    print(f"#{tc} {total}")
