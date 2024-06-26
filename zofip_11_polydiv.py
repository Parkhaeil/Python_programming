
def Div(u,g):
    n = len(u)-len(g)      # 몫의 최고차항 차수
    f = []
    for _ in range(n+1):
        s = u[0]//g[0]; f.append(s)
        for i in range(len(g)):
            u[i] -= g[i] * s
        del u[0]
    return f , u

def del0(r):                # 나머지에서 앞에 0 다 지워주는 함수
    if set(r) == {0}: r = [0]
    else :
        while r[0] == 0:
            del r[0]
    return r

u = list(map(int, input().split()))
g = list(map(int, input().split()))
f, r = Div(u,g)
print(*f)
print(*del0(r))