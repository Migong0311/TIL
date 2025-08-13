def func1(a, b, c):
    print('1번함수시작', a, b, c)
    func2(a, b, c)
    print('1번함수종료', a, b, c)


def func2(a, b, c):
    print('2번함수시작', a, b, c)
    func3(a, b, c)
    print('2번함수종료', a, b, c)


def func3(a, b, c):
    print('3번함수시작', a, b, c)

    print('3번함수종료', a, b, c)


func1(1, 2, 3)
"""
순서

[시작]
func1 -> func2 -> func3

[종료]
func3 -> func2 -> func1 // 스택 형식으로 종료 시 pop 되는걸 알 수 있음

[출력]
1번함수시작 1 2 3
2번함수시작 1 2 3
3번함수시작 1 2 3
3번함수종료 1 2 3
2번함수종료 1 2 3
1번함수종료 1 2 3
"""