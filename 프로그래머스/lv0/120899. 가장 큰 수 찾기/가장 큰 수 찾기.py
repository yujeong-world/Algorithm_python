def solution(array):
    answer = []
    max = array[0]
    ind = 0
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
            ind = i
    answer.append(max)
    answer.append(ind)
    return answer