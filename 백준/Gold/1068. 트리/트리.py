import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(n)] #-1 0 0 2 2 4 4 6 6 입력 -> 그래프 저장 [[1, 2], [], [3, 4], [], [5, 6], [], [7, 8], [], []]

for node_num,i in enumerate(sys.stdin.readline().rstrip().split()):
    if int(i)==-1 : continue
    tree[int(i)].append(node_num) #트리 노드 초기회
r = int(sys.stdin.readline().rstrip())

leaf_list = [] #리프 노드 리스트

def remove_tree(tree,r): #노드 제거
    stack = deque([(r)])
    while stack:
        cn = stack.pop()
        while tree[cn]:
            nn = tree[cn].pop()
            stack.append(nn)
        for node in tree:
            if cn in node:
                node.remove(cn)
        tree[cn].append(-100) #쓰레기값 넣기(나중에 리프노드 계산 때 편리하게 하기 위함)

    for node_num, node in enumerate(tree):
        if len(node) == 0:
            leaf_list.append(node_num)
    return len(leaf_list)

print(remove_tree(tree,r))
