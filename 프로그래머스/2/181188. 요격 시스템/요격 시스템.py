def solution(targets):
    answer_set = set()
    targets.sort(key=lambda x: (x[0],x[1]))
    tmp_answer = [0,0]

    for i in range(len(targets)):
        if targets[i][0] < tmp_answer[1]:  # 이미 겹치는 경우에는 continue
            continue
        elif targets[i][1] < tmp_answer[1]:
            continue
        else:
            tmp_answer = targets[i]
        # print("se", targets[i])
        j = i
        while targets[j][0]<targets[i][1]:
            # print("비교대상",targets[j][0],targets[i][1])
            if targets[j][0] < targets[i][1] and targets[j][0] >= targets[i][0]:  # 다른 미사일이 겹치는 경우. 오른쪽으로 겹칠 때
                if targets[j][0] > targets[i][0] and targets[j][1] <= targets[i][1]:  # 내부에 속해 있는 경우
                    # print("내부", targets[j])
                    tmp_answer[0] = targets[j][0]
                    tmp_answer[1] = targets[j][1]
                else:  # 오른쪽으로 겹치는 경우
                    # print("오른쪽", targets[j])
                    tmp_answer[0] = targets[j][0]  # 뒤에있는 미사일의 시작부분으로 범위 좁히기

            j+=1
            if j==len(targets):
                break

        answer_set.add(tuple(tmp_answer))
    # print(answer_set)
    return len(answer_set)