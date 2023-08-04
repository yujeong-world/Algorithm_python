def solution(num_list):
    answer = 0
    length = len(num_list)
    if length >10:
        for i in range(length):
            answer+= num_list[i]
    if length<=10:
        answer=1
        for i in range(length):
            answer *=num_list[i]
    return answer