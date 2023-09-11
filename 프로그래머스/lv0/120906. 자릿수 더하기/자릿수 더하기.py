def solution(n):
    answer =0
    n = str(n)
    integer_list = [int(char) for char in n]
    for i in range(len(integer_list)):
        answer+=integer_list[i]
    


    return answer