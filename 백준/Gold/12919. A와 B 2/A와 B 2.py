from collections import deque

def can_transform(S, T):
    queue = deque([T])
    visited = set([T])  # To avoid processing the same state multiple times
    while queue:
        current = queue.popleft()

        # If current equals S, transformation is possible
        if current == S:
            return 1

        # Transformations
        if current.endswith('A') and current[:-1] not in visited:  # Remove 'A'
            queue.append(current[:-1])
            visited.add(current[:-1])
        if current.startswith('B') and current[1:][::-1] not in visited:  # Remove 'B' and reverse
            queue.append(current[1:][::-1])
            visited.add(current[1:][::-1])

    return 0  # Transformation not possible


# 입력 처리
S = input().strip()
T = input().strip()

# 결과 출력
print(can_transform(S, T))