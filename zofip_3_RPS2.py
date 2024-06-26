people = list(input().split( ))
people = set(people)

if len(people) != 2:
    print('D')

elif "S" not in people:
    print('P')

elif "R" not in people:
    print('S')

elif "P" not in people:
    print('R')

