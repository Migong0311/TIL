# 병합 정렬을 연습하는 로직입니다
import sys

sys.stdin = open('test.txt', 'r')
'''
문제
N개의 정수 주어짐
병합 정렬을 이용하여 정수를 오름차순으로 정렬

병합정렬은 2개의 단계로 나눌 수 있음

분할 : 리스트 **절반**
병합 : 분할된 두 리스트 정렬하면서 합침

입출력 예제

입력
2
8
69 10 30 2 16 8 31 22
5
5 1 4 2 3

출력
#1 2 8 10 16 22 30 31 69
#2 1 2 3 4 5

'''

T = int(input())


# 병합 담당 함수: 두 정렬된 리스트를 하나로 합침
def merge(left, right):
    result = []  # 병합 결과 담을 리스트
    i, j = 0, 0  # 좌,우 인덱스 초기화

    while i < len(left) and j < len(right):  # 양쪽 리스트 모두 값이 남아있을때
        # 안정정렬을 위한 이상 사용
        if left[i] <= right[j]:
            result.append(left[i])  # 더 작은 값을 결과에 추가
            i += 1
        else:  # 오른쪽 값 추가
            result.append(right[j])
            j += 1

    # 남은 요소들 처리(한쪽 리스트가 끝난 경우)
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# 병합 정렬 함수
def merge_sort(array):
    if len(array) <= 1:  # 원소가 하나 이하라면 정렬 불필요
        return array

    mid = len(array) // 2  # 중간 인덱스 계산
    left = merge_sort(array[:mid])  # 왼쪽 절반 재귀 정렬
    right = merge_sort(array[mid:])  # 오른쪽 절반
    return merge(left, right)  # 두개를 서로 합침


for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = merge_sort(arr)
    print(f'#{t}', *sorted_arr)
