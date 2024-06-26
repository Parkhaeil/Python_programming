# 1월 1일이 월요일이면 모든 일수를 더하고 7로 나눈 수
# 의 나머지가 0이면 일요일, 1이면 월요일 6이면 토요일이다.

month = int(input())
days  = list(map(int,input().split( )))
yoil  = input()
m1,d1 = map(int, input().split())
m2,d2 = map(int, input().split())
m3,d3 = map(int, input().split())

seven = ["월","화","수","목","금","토","일"]
stdmonth = [m1,m2,m3]
stdday   = [d1,d2,d3]
index = seven.index(yoil)


for a in range(3):
    ttlyoil = 0
    final = 0

    if stdmonth[a]>month or stdday[a]-days[stdmonth[a]-1]>0:
        print('땡')

    else:
        for i, w in enumerate(days):
            if stdmonth[a] == i+1:
                ttlyoil = (ttlyoil+stdday[a]-1)%7
                break
            ttlyoil += w


        final = (index + ttlyoil)%7

        print(seven[final])



