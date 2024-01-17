def solution(progresses, speeds):
    countList = []
    temp = progresses
    while temp:
        for i in range(len(temp)):
            temp[i] += speeds[i]

        count=0
        while temp and temp[0] >= 100:
            temp.pop(0)
            speeds.pop(0)
            count += 1
            
        if count > 0:
            countList.append(count)
                      
    return countList