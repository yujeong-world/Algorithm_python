def solution(num_list):
    answer=-1
    num=0
    while num<len(num_list):
        if num_list[num]<0:
            answer= num
            break
        num+=1
        
            
    return answer