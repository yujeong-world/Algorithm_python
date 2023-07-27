def solution(arr):
    if(len(arr)==1):
        answer = []
        answer.append(-1)
    else:
        answer = arr
        min=arr[0]
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
        answer.remove(min)
    return answer