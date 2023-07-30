def solution(s):
    answer = ''
    temp = s.split(' ')
    ex = []
    for i in range(len(temp)):
        ex.append(temp[i].capitalize())
    answer = ' '.join(ex)
    return answer