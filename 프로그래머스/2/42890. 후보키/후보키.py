from itertools import combinations

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    
    # 가능한 모든 컬럼 조합을 저장
    all_combinations = []
    for i in range(1, col_len + 1):
        all_combinations.extend(combinations(range(col_len), i))
    
    # 후보키 리스트
    candidate_keys = []
    
    # 각 조합별로 유일성 및 최소성 확인
    for comb in all_combinations:
        # 해당 조합으로 튜플을 만들었을 때, 유일한지 확인
        unique_rows = set(tuple(relation[row][col] for col in comb) for row in range(row_len))
        
        # 유일성을 만족하는 경우
        if len(unique_rows) == row_len:
            # 최소성 확인
            is_minimal = True
            for key in candidate_keys:
                if set(key).issubset(comb):
                    is_minimal = False
                    break
            # 최소성을 만족하면 후보키로 추가
            if is_minimal:
                candidate_keys.append(comb)
    
    return len(candidate_keys)

# 예시 실행
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))  # 출력: 2
