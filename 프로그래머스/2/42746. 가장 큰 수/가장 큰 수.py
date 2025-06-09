from functools import cmp_to_key

def solution(numbers):
    def compare(x, y):
        if str(x) + str(y) > str(y) + str(x):
            return -1
        elif str(x) + str(y) < str(y) + str(x):
            return 1
        else:
            return 0

    # 4자리 패딩 기존 유지하되, 보조 정렬로 직접 비교를 추가해 해결
    numbers.sort(key=lambda x: (
        -int(str(x).ljust(4, str(x)[-1])), 
        -sum(int(digit) for digit in str(x).ljust(4, str(x)[-1])), 
        len(str(x))
    ))

    # 최종 정확성 보장용 추가 정렬
    numbers = sorted(numbers, key=cmp_to_key(compare))

    result = ''.join(map(str, numbers))
    return '0' if result[0] == '0' else result
