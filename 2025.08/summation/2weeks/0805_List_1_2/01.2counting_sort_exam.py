def counting_sort(data, temp, k):
    # data : 정렬하고 싶은 대상(배열,인덱스)
    # temp : 정렬 결과 (배열,리스트)
    # K : 정렬 대상 배열 안에 들어있는 정수 중 최대값
    # K == 카운트 배열의 크기

    count = [0] * (k + 1)
    # count : 카운트배열(각원소의 등장 횟수를 세기 위해)
    # c[x] : 정수 x의 등장 횟수
    # c[3] : 숫자 3이 data배열 안에 몇개 있었는지 기록

    # 1. 모든 원소의 등장 횟수 리스트
    for num in data:
        count[num] += 1

    # 2. 각 원소의 등장횟수를 더해서 누적 합 계산
    # 각 원소가 정렬후에 들어갈 자리 위치를 계산
    # 어떤 숫자 x보다 작은 숫자가 몇개 있는지 알고있다면
    # x의 정렬 후 자릴 특정할 수 있다.
    for i in range(1, k + 1):
        count[i] += count[i - 1]

    # 3. 뒤에서부터 data를 확인하면서 count 배열을 보고
    # 자리를확인 자리(인덱스) = count[숫자] - 1
    # count[x] 에 가서 값 확인하고여기서 -1 한 위치(인덱스)
    # 정렬 후 위치가 된다
    # 뒤에서 부터 확인하는 이유는 -> 안정 정렬을 위해서(원래 순서를 보장)
    for i in range(len(data) - 1, -1, -1):
        # data[i]에 있는 숫i자의 정렬 후 위치는 어딘가?
        # count에서 data[i]에 있는 숫자의 값을 확인 -1한 자리가 정렬 후 위치
        x = data[i]
        count[x] -= 1

        # 정렬 후결과 배열 temp에 data[i] 놓기
        # x : data[i]
        # count[x] : x(data[i])가 들어갈 위치(인덱스)
        temp[count[x]] = x

    return temp


nums = [0, 4, 1, 3, 1, 2, 4, 1]  # 정렬 대상 배열
result = [0] * 8
print(counting_sort(nums, result, max(nums)))
