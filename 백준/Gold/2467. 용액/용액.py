def find_closest_to_zero(N, solutions):
    left, right = 0, N - 1
    min_sum = float('inf')
    result = (0, 0)

    while left < right:
        current_sum = solutions[left] + solutions[right]
        
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result = (solutions[left], solutions[right])
        
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            return result

    return result

# 입력 처리
N = int(input())
solutions = list(map(int, input().split()))

# 결과 출력
answer = find_closest_to_zero(N, solutions)
print(f"{answer[0]} {answer[1]}")