def solution(s):
    answer = s.split(" ")
    length = len(answer)
    result=[]
    for i in range(length):
        for j in range(len(answer[i])):
            if j % 2 ==0:
                temp = answer[i][j].upper()
                result.append(temp)
            else:
                temp = answer[i][j].lower()
                result.append(temp)
        result.append("*")
    result.pop()
    result = ''.join(result)
    result = result.replace("*", " ")

    return result