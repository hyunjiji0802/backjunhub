def solution(s):
    # 압축할 수 있는 최소 단위는 1부터 최대 문자열 길이의 절반까지
    min_length = len(s)  # 압축되지 않는 경우의 길이 (최대값)

    for size in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:size]  # 첫 번째 단위를 미리 설정
        count = 1  # 반복된 횟수

        # size 단위로 문자열을 나누어 반복 처리
        for i in range(size, len(s), size):
            current = s[i:i + size]  # 현재 단위를 가져옴

            # 이전 단위와 같으면 반복 횟수 증가
            if prev == current:
                count += 1
            else:
                # 이전 단위와 다르면 지금까지의 압축된 내용을 저장
                if count > 1:
                    compressed += str(count) + prev  # 2번 이상 반복된 경우 숫자와 함께
                else:
                    compressed += prev  # 반복되지 않았으면 그냥 추가

                # 현재 단위를 새로운 단위로 변경
                prev = current
                count = 1  # 반복 횟수 초기화

        # 마지막 남은 단위 처리
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        min_length = min(min_length, len(compressed))  # 가장 짧은 압축 결과 저장

    return min_length