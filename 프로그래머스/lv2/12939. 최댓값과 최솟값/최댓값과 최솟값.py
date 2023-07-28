def solution(s):
    answer = ''
    len(str(s))
    r = s.split(' ')
    r = list(map(int, r))
    r.sort()
    
    a= r[0]
    b= r[len(r)-1]
    answer =str(a)+' '+str(b)
    return answer