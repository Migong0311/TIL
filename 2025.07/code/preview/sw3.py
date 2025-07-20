N = int(input())
if N < 9 or N > 199 or N % 2 == 0:
    print("Input out of range")
else:
    scores = list(map(int, input().split()))
    
    if len(scores) != N:
        print("점수의 개수가 잘못되었습니다.")
    else:
        scores.sort()
        median = scores[N // 2]
        print(median)
