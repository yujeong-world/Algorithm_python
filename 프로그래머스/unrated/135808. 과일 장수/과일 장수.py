def solution(k, m, score):
    answer = 0
    length = len(score)//m #박스 묶음의 수
    
    score.sort(reverse = True)
    count=0
    orginM= m
    #for i in range(length):
    while m <=len(score):
        answer+= score[m-1] * orginM
        m= m+orginM
    

    
    return answer