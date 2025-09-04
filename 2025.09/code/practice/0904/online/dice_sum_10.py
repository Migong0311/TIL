# 주사위 3개를 던져서 합이 10 이하인 케이스 수

path = []  # 무조건 기존 주사위를 기록해놔야함?

result = 0  # 누적 합

print('====결과====')


def recur(cnt):
    global result
    # 이미 10을 넘은 경우 바로 리턴
    if sum(path)> 10:
        return

    if cnt == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1
        return

    for i in range(1, 7):
        path.append(i)
        recur(cnt + 1)
        path.pop()


recur(0)
print()
print('====결과 개수======')
print(result)
