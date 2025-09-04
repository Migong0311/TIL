N = 5

arr = [1, 2, 3, 4, 5]

b = [0] * 5


#
# for i in range(N):
#     b[i] = arr[i]
#     print(b)

def recur(x):
    if x >= N:
        return

    b[x] = arr[x]

    recur(x + 1)


recur(0)
print(b)
