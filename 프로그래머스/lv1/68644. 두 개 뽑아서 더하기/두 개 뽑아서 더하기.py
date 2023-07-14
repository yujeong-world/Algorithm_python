def solution(numbers):
    answer = set()
    last = len(numbers)
    for i in range(last):
        if i!=last:
            for j in range(i+1,last):
                answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort()
    return answer