def solution(s):
    answer = []
    result=[]
    temp = ''
    num1 = [0,1,2,3,4,5,6,7,8,9]
    num2 = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8','nine':'9'}
    for i in range(len(s)):
        temp += s[i]
        if temp in num2.keys():
            answer.append(num2[temp])
            temp = ''
        if temp in num2.values():
            answer.append(temp)
            temp=''
            
    answer = ''.join(answer)
    answer = int(answer)
            
            
            
    return answer