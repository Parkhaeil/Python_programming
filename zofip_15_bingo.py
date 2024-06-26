##import numpy as np
##
###가로,세로,대각선 왕중왕전
##
##def value(a,b,cnt):
##    if a > b:
##        b = a
##        cnt = 1
##    elif a == b:
##        cnt += 1
##    return a,b,cnt
##
##def rowvalue(k):
##    cnt = 0
##    max_cnt = 0
##    for i in k:
##        if i == 1:
##            cnt += 1
##            max_cnt = max(cnt, max_cnt)
##        else:
##            cnt = 0
##    return max_cnt
##
##def solve(arr,a,b,cnt):
##    (n,m) = arr.shape
##    ttl = []
##    for i in range(n):
##        ttl.append(list(arr[i]))
##    for j in range(m):
##        ttl.append(list(arr[:,j]))
##
##    reverse = np.fliplr(arr)
##    for k in range(-n+1, m):
##        ttl.append(list(np.diag(arr,k)))
##        ttl.append(list(np.diag(reverse,k)))
##
##    for l in ttl:
##        a = rowvalue(l)
##        _,b,cnt = value(a,b,cnt)
##
##    return b,cnt
##
##
##
###입력한 표 arr만들기
##bingo = []
##while True:
##    try:
##        line = list(input())
##        bingo.append(line)
##    except:
##        break
##
##arrr = np.array(bingo, dtype=np.int8)
##print(*solve(arrr,0,0,0))

import numpy as np

def value(a, b, cnt):
    if a > b:
        b = a
        cnt = 1
    elif a == b:
        cnt += 1
    return a, b, cnt

def rowvalue(k):
    max_cnt = 0
    cnt = 0
    for i in k:
        if i:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 0
    return max_cnt

def solve(arr):
    n, m = arr.shape
    ttl = []
    for i in range(n):
        ttl.append(list(arr[i]))
    for i in range(m):
        ttl.append(list(arr[:, i]))
    reverse = np.fliplr(arr)
    for k in range(-n+1, m):
        ttl.append(list(np.diag(arr, k)))
        ttl.append(list(np.diag(reverse, k)))

    b = 0
    cnt = 0
    for l in ttl:
        a = rowvalue(l)
        _, b, cnt = value(a, b, cnt)

    return b, cnt

# 입력한 표 arr 만들기
bingo = []
while True:
    try:
        line = list(input())
        bingo.append(line)
    except:
        break

arrr = np.array(bingo, dtype=np.int8)
print(*solve(arrr))
