def coupon(c,pri,x):
    try :

        #x가 포함되어있는 케이스
        if pri[x] <= c:
            c1 = c - pri[x]
            newpri = pri[x+1:]
            newcou = coupon(c1,newpri,x+1)
            for j in range(newcou):
                newcou[j].append(x+1)

            try :
                myend += newcou
            except TypeError:
                pass

        #x가 포함되어있지 않은 케이스
        newpri_two = pri[x+1:]
        myend += coupon(c,newpri_two,x+1)


    except IndexError:
        return(myend)




k, c = map(int,input().split())
pri = []
global myend = []
for i in range(k):
    pri.append(int(input()))


print(coupon(c,pri,0))
