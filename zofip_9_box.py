
def box_test():
    point = list(map(int,input().split()))
    xpoint = point[::3]
    ypoint = point[1::3]
    zpoint = point[2::3]

    #a,b 박스의 x길이와 y길이와 Z길이
    ax = xpoint[1] - xpoint[0]
    bx = xpoint[3] - xpoint[2]
    ay = ypoint[1] - ypoint[0]
    by = ypoint[3] - ypoint[2]
    az = zpoint[1] - zpoint[0]
    bz = zpoint[3] - zpoint[2]

    ttlx = ax + bx
    ttly = ay + by
    ttlz = az + bz

    #두 개의 사각형을 에워싸는 큰 사각형 만드는 과정
    srt_xpoint = sorted(xpoint)
    srt_ypoint = sorted(ypoint)
    srt_zpoint = sorted(zpoint)

    bigx = srt_xpoint[-1] - srt_xpoint[0] # 큰 사각형 x 길이
    bigy = srt_ypoint[-1] - srt_ypoint[0] # 큰 사각형 y 길이
    bigz = srt_zpoint[-1] - srt_zpoint[0]

    lst = [bigx==ttlx,bigy==ttly,bigz==ttlz]
    x =  lst.count(1)
    if (bigx > ttlx) or (bigy > ttly) or (bigz > ttlz) :
        print("NULL")
    elif x == 3:
        print("POINT")
    elif x == 2:
        print("LINE")
    elif x == 1:
        print("FACE")
    elif (bigx < ttlx) and (bigy < ttly) and (bigz < ttlz) :
        print("VOL")



for _ in range(4):
    box_test()
