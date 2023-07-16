def solution(array, commands):
    answer = []
    length = len(commands)
    
    for x,y,z in commands:
        temp = array[:]
        temp1 = temp[x-1:y]
        temp1.sort()
        answer.append(temp1[z-1])
        
    return answer