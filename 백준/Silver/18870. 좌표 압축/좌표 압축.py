import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
sort_arr=sorted(list(set(arr)))


def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if element == some_list[mid_index]:
            return mid_index

        elif element < some_list[mid_index]:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return None


for i in range(N):
    arr[i]=binary_search(arr[i],sort_arr)

print(" ".join(map(str,arr)))