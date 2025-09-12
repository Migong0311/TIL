# 중복 순열
# 0,1,2  3개의 카드가 존재


path = []  # 방문한 카드를 저장


# 기저조건은 2개의 카드를 모두 뽑았다면 종료
# 시작점 : 0개의 카드를 고른 상태부터 시작
# 다음 재귀호출 구조 0,1,2 카드 중 하나를 뽑는다

def recur(cnt):
    if cnt == 2:
        print(*path)
        return

    # 0,1,2 중 하나를 선택
    # path.append(0)
    # recur(cnt + 1) # 하나 선택했으니 다음 선택으로 이동
    # path.pop()
    #
    # path.append(1)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(2)
    # recur(cnt + 1)
    # path.pop()

    # 위 과정을 for문으로 한번에 관리

    for i in range(3):
        path.append(i)
        recur(cnt + 1)
        path.pop()

    
recur(0)
