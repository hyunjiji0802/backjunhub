def solution(phone_book):
    phone_book.sort(key=lambda x:(x, len(x)))
    phone_book_dic = {}
    #딕셔너리에 각 전화번호 넣기
    for phone_number in phone_book:
        phone_book_dic[phone_number] = True
        for i in range(1,len(phone_number)+1):
            prefix = phone_number[:i]
            if phone_book_dic.get(prefix):
                if prefix == phone_number: continue
                else:
                    #print(phone_number)
                    return False
    return True