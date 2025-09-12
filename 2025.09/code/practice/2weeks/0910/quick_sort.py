arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]

'''
일반적으로 피벗을 젤 중앙으로 위치해서 하는게 성능이 젤 좋음
비추지만 만일 피벗을 젤 왼쪽에서 시작하면 
pivot = arr[left]  # 피벗을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right

반대로 오른쪽이면
 pivot = arr[right]  # 피벗을 제일 오른쪽 요소로 설정
    i = left
    j = right - 1
이렇게 지정이 가능함 
'''
# 피벗 : 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition1(left, right):
    mid = (left + right) // 2
    p = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left] # 필요시 중간 요소를 왼쪽으로 이동

    i = left + 1  # 피벗 옆
    j = right  # 젤 끝에

    while i <= j:  # 교차가 되면 끝
        # i는 피벗보다 큰 값을 검색 (작거나 같으면 i += 1)
        while i <= j and arr[i] <= p:
            i += 1
        # j는 피벗보다 작은 값을 검색 (크거나 같으면 j -= 1)
        while i <= j and arr[j] >= p:
            j -= 1

        if i < j:  # swap
            arr[i], arr[j] = arr[j], arr[i]
    # 피벗과 j의 위치를 swap
    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        p = hoare_partition1(left, right)
        quick_sort(left, p - 1)
        quick_sort(p + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
