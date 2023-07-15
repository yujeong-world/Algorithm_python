def solution(nums):
    answer = 0
    result = []
    #더할 수 있는 경우의 수를 모두 찾는다.
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                result.append(nums[i]+nums[j]+nums[k])

    
    #소수 찾기
    for i in range(len(result)):
        count =0
        for j in range(2, result[i]):
            if result[i] % j == 0:
                count+=1
        if count==0 :
            answer+=1
    return answer