import math

for _ in range(3):
    a,b,n = map(int,input().split())

    setaone = math.atan(b/a)
    setatwo = math.atan(b/(n-a))
    setattl = 2*(setaone + setatwo)

    line = b*setattl + a + (n-a)
    x = math.ceil(line)
    print(x)