a=int(input())
if a < 1 or a > 9999:
    print("Input out of range")
else:
    total = 0
    while a > 0:
        total += a % 10   # 일의 자리 더하기
        a //= 10          # 한 자리씩 줄이기
    print(total)