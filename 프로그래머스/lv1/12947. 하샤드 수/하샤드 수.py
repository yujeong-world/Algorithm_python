def solution(x):
    answer = True
    temp = x
    x = list(map(int,str(x)))
    print(x)
    result =0
    for i in range(len(x)):
        result += x[i]
    if temp % result ==0:
        answer = True
    else:
        answer = False
    return answer