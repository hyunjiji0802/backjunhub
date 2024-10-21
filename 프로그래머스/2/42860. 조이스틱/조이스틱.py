def solution(name):
    # str_len = len(name.rstrip('A'))  # 마지막 A는 고려하지 않은 문자열 길이
    str_len = len(name)
    name = list(map(lambda x: min(ord(x) - 65, abs(26 - (ord(x) - 65))),
                    name))  # 각 글자마다 이동해야하는 조이스틱 조작 횟수 리스트, A로부터 더 가까운 방향(위/아래)까지 고려
    move = str_len - 1  # 최대 이동 거리

    for i in range(str_len):  #오른쪽으로 계속 이동
        id = i + 1
        while id < str_len and name[id] == 0:  # i 다음에서부터 연속되는 A 자리수 구하기
            id += 1
        # print(move ,i * 2 + str_len - 1 - id,i+2*(str_len-id))
        move = min([move, i * 2 + (str_len - id), i+2 * (str_len - id)]) # i 위치에서 오른쪽으로 가는 이동 횟수 vs 왼쪽으로 돌아서 연속되는 A 끝난 후 까지 가는 이동 횟수

    return move + sum(name)