import sys
n= int(input())
data = [int(input()) for _ in range(n)]

data.sort()

for i in range(len(data)):
    print(data[i])
