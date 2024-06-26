
shooting = input()
x = 0
score = 0
combo = 0

if shooting[x] == "o":
    score -= 1
else:
    score += 1
    combo += 1

x += 1

while 1 <= x < len(shooting) :
    if shooting[x-1] == "o":

        if shooting[x] == "o":
            score -= 1
        else:
            score += 1
            combo += 1

    elif shooting[x-1] == "h":
        if shooting[x] == "o":
            score -= 1
            combo = 0
        else:
            combo += 1
            score = score + combo

    x += 1

print(score)



