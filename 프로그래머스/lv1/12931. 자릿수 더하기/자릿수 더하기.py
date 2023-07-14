def solution(n):
    a = list(map(int, str(n)))
    answer=0
    for i in a:
        answer+=i
    return answer