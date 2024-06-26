
def rectangle_test():
    point = list(map(int,input().split()))
    xpoint = point[0::2]
    ypoint = point[1::2]

    #a사각형의 x길이와 y길이, b사각형의 x길이와 y길이 구하기
    ax = xpoint[1] - xpoint[0]
    bx = xpoint[3] - xpoint[2]
    ay = ypoint[1] - ypoint[0]
    by = ypoint[3] - ypoint[2]

    ttlx = ax + bx
    ttly = ay + by

    #두 개의 사각형을 에워싸는 큰 사각형 만드는 과정
    srt_xpoint = sorted(xpoint)
    srt_ypoint = sorted(ypoint)

    bigx = srt_xpoint[-1] - srt_xpoint[0] # 큰 사각형 x 길이
    bigy = srt_ypoint[-1] - srt_ypoint[0] # 큰 사각형 y 길이


    if ( bigx == ttlx ) and ( bigy == ttly ):
        print("POINT")
    elif ( bigx == ttlx ) or ( bigy == ttly ):
        print("LINE")
    elif ( bigx < ttlx ) or ( bigy < ttly ):
        if ( bigx > ttlx ) or ( bigy > ttly ):
            print("NULL")
        else:
            print("FACE")
    else:
        print("NULL")

for _ in range(4):
    rectangle_test()
