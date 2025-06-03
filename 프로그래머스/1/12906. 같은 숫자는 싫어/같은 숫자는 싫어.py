def solution(arr):
    answer = []
    while arr:
        item = arr.pop()
        
        #answer 가 비어있거나 동일한 연속 수가 아니라면 append
        if (len(answer) == 0) or (answer[-1] != item):
            answer.append(item)
            
    #정답배열 순서 뒤집기
    answer.reverse()
    return answer