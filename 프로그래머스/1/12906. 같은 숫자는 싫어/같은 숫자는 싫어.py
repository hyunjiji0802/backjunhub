def solution(arr):
    answer = []
    prev_num = -1 #비교할 숫자
    while arr:

        pop_num = arr.pop()
        if pop_num == prev_num : #원소가 연속되는 경우
            pass
            # if answer
            # answer.append(prev_num) #이전에 추출한 원소를 answer에 담기
        else: #다음 원소가 연속된 숫자가 아닌경우
            answer.append(pop_num)
        prev_num = pop_num
    answer.reverse()
    return answer