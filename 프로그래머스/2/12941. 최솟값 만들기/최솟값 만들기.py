def solution(A,B):
    answer = 0
    #먼저 정렬해준다.
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer