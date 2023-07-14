def solution(s):
    answer = True
    count = {"p":0, "P":0, "y":0, "Y":0}
    countP =0
    countY = 0
    for i in s:
        if i in count.keys():
            if i == "p" or i =="P":
                countP +=1
            else:
                countY +=1
    if countP == countY:
        return True
    else:
        return False

    return True