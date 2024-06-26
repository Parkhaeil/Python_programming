
def poly(f,g):
    ans = [0]*(len(f)+len(g)-1)
    for i in range(len(f)):
        for j in range(len(g)):
            ans[i+j] += f[i] * g[j]
    return ans

lines = []
while True:
    try:
        myinput = list(map(int,input().split()))
        lines.append(myinput)
    except :
        break

ans = poly(lines[0], lines[1])
for i in range(2, len(lines)):
    ans = poly(ans,lines[i])

if set(ans) == {0}: print(0)
else:               print(*ans)