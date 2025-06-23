def solution(phone_book):
    # 1. 문자열 오름차순 정렬
    phone_book.sort()
    # 2. 기준  pointer
    p1, p2 = 0, 1

    # 각 전화번호마다 반복
    while p1 < p2 and p2 < len(phone_book):
        if len(phone_book) == 1:
            return True

        # 접두어라면
        if (len(phone_book[p1]) <= len(phone_book[p2])) and (phone_book[p1] == phone_book[p2][:len(phone_book[p1])]):
            return False
        else:
            p1 = p2
            p2+=1

    return True
