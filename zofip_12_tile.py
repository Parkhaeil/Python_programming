# 부산대 자유관, 1136호에서
lst = list(map(int,input().split()))
myoutput = [0]*lst[0]

for i in range(len(myoutput)):
    for w in lst:
        if i+1 <= w:
            myoutput[i] += 1
print(*myoutput,0)



