def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        new_arr = array[i-1:j]
        # print(new_arr)
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer