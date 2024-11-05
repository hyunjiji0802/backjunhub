import re

def split_file(file):
    tmp = re.split(r"([0-9]+)",file, maxsplit=1)
    print(tmp)
    return tmp

def solution(files):
    split_list =[]
    
    for file in files:
        split_list.append(split_file(file))
    #x = ['img', '10', '.jpg']
    #x[0] = 
    #split_list.sort(key = lambda x:(str(x[0]).upper(), int(re.sub(r"^0+","",x[1]))))
    split_list.sort(key = lambda x:( x[0].upper(), int(x[1]) ))
    answer = []
    for splits in split_list:
        answer.append(''.join(splits))

    return answer