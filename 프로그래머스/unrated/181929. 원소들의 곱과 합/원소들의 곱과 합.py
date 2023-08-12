def solution(num_list):
    answer = 0
    temp = 1
    plus = 0
    for i in range(len(num_list)):
        temp *= num_list[i]
        plus += num_list[i]
    if temp > (plus*plus):
        answer = 0
    else:
        answer =1
    return answer