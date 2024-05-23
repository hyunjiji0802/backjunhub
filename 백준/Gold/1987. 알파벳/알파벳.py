import sys
r,c = map(int,sys.stdin.readline().rstrip().split())
board = []
for _ in range(r):
    board.append(list(input()))

    #상 하 좌 우
dc=[0,0,-1,1]
dr=[-1,1,0,0]

def dfs(cur_c, cur_r):
    max_len = 1
    stack = set([(cur_c,cur_r, board[cur_r][cur_c])]) #set으로 구현 (현재 컬럼, 현재 로우, 알파벳(A~Z))을 담은 셋
    while stack:
        cur_c,cur_r, alpha_visited = stack.pop()
        max_len = max(max_len, len(alpha_visited))
        if max_len==26:
            return 26
        for i in range(4):
            nc, nr = cur_c + dc[i], cur_r + dr[i]
            if 0 <= nc < c and 0 <= nr < r and board[nr][nc] not in alpha_visited:  # 알파벳 방문리스트에 없고(처음 밟는 알파벳) 범위 벗어나지 않으면
                stack.add((nc,nr,alpha_visited + board[nr][nc]))

    return max_len

print(dfs(0,0))