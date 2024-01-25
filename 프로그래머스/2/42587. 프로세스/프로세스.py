def solution(priorities, location):
    answer = 0
    length = len(priorities) #리스트의 초기 길이를 구한다.
    seqNum = []
    for i in range(length): #순서 번호 저장 리스트를 만들어준다.
        seqNum.append(i) 
    print(seqNum)
    count =0
    
    while priorities:
        maxVal = max(priorities) #초기에 최댓값을 구함
        if priorities[0] == maxVal:
            priorities.pop(0)
            a = seqNum[0]
            seqNum.pop(0)
            count+=1
            if a == location:
                print(seqNum)
                return count
            
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            a = seqNum.pop(0)
            seqNum.append(a)
                
    return answer


        