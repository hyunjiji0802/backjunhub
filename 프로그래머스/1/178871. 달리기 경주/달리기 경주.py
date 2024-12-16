def solution(players, callings):
    # 선수들의 초기 순위 리스트
    index_map = {player: i for i, player in enumerate(players)}  # 선수 이름 -> 순위 인덱스
    
    for calling in callings:
        # 호출된 선수의 현재 순위 인덱스
        idx = index_map[calling]

        # 앞선 선수 이름
        prev_player = players[idx - 1]

        # 두 선수를 위치 변경
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        # 순위 인덱스를 업데이트
        index_map[calling] = idx - 1
        index_map[prev_player] = idx

    return players
