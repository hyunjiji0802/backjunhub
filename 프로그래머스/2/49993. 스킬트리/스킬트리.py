def solution(skill, skill_trees):
    answer = 0
    for cur_skill_tree in skill_trees:
        cur_skill_tree_id = 0
        stack = []
        possible = True

        while cur_skill_tree_id < len(cur_skill_tree):

            if cur_skill_tree[cur_skill_tree_id] in skill: #스킬 트리 확인
                stack.append(cur_skill_tree[cur_skill_tree_id])
            cur_skill_tree_id+=1 #계속해서 다음 스킬 뭐 찍는지 확인
        #stack = ''.join(stack)
        skill_stack = list(skill)
        while stack:
            s = stack.pop(0)
            a = skill_stack.pop(0)
            if s!= a:
                possible=False
                break
        if possible:
            answer+=1

    return answer