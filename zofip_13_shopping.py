
stuffnum = []
def similarity(a,b):
    gyeo = len(a&b)
    hap = len(a|b) + 1
    return(gyeo,hap)

name = []
while True:
    try :
        line = list(input().split())
        if line[0] not in name:
            name.append(line.pop(0))
            stuffnum.append(set(line))
        else:
            index = name.index(line[0])
            line.pop(0)
            stuffnum[index] = (stuffnum[index] | set(line))

    except :
        break

gyeo1 = 0
hap1 = 1
mystd = []

for i in range(len(stuffnum)-1):
    for j in range(i+1, len(stuffnum)):
        gyeo2,hap2 = similarity(stuffnum[i],stuffnum[j])

        if gyeo1/hap1 < gyeo2/hap2:
            mystd = [[name[i],name[j]]]

        elif  gyeo2/hap2 == gyeo1/hap1:
            mystd.append([name[i],name[j]])

        gyeo1 , hap1 = gyeo2 , hap2


n = 0
while True:
    try:
        mystd[n].sort()
        print(mystd[n][0],mystd[n][1])
        n+=1
    except:
        break




