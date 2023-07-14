def solution(n, m):
    answer = []
    n1 = n
    m1 =m
    if n<m:
        n,m=m,n
    a=0
    while a==0:
        r = n%m
        if r ==0:
            answer.append(m)
            a=1
        else:
            n,m = m,r
            continue
    if m1 == 1 or m1 ==2:
        min = (n1*m1)
        answer.append(min)
    else:
        min = (n1*m1)/answer[0]
        answer.append(min)
        
    return answer