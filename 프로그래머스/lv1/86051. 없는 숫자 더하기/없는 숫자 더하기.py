def solution(numbers):
    answer = [i for i in range(10)]
    answer2=0
    for i in range(len(numbers)):
        if numbers[i] in answer:
            answer.remove(numbers[i])
    for i in answer:
        answer2 += i
    return answer2