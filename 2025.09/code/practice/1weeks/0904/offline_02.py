N = 5
A = [1, 2, 3, 4, 5]

# 찾고자 하는 값
key = 4

# for

# for i in range(N):
#     if A[i] == key:
#         print('find', i)
#         break
# else:
#     print('None')


# recursion
def search(x):
    # 종료조건
    if A[x] == key:
        print('find', x)
        return
    if x == N:
        print('None')
        return
    # x값이후 1 증가하면서 search
    search(x + 1)


search(0)
